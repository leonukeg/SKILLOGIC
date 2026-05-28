import reflex as rx
import sys
import io
import contextlib
import traceback
from typing import List, Dict, Any
from SKILLOGIC.data.lesson_1_1 import LESSON_1_1
from SKILLOGIC.state.auth_state import AuthState
from SKILLOGIC.lib.supabase_client import fetch_user_profile, update_user_progress

# Define the sequence of phases
PHASES = [
    "1_hook",
    "2_challenge",
    "3_theory",
    "4_guided_build",
    "5_struggle",
    "7_build",
    "8_retrieval"
]
# 6_feedback is not a separate phase in the UI, it's triggered when struggle fails.

class LessonState(rx.State):
    """Manages the state for the interactive learning session."""
    current_phase_index: int = 0
    
    # Code editor state
    user_code: str = ""
    terminal_output: str = ""
    
    # Parsons problem state
    parsons_blocks: List[Dict[str, str]] = []
    user_order: List[str] = []  # List of block IDs
    
    # Validation state
    is_success: bool = False
    feedback_message: str = ""
    show_pro_feedback: bool = False
    
    @rx.var
    def current_phase_key(self) -> str:
        return PHASES[self.current_phase_index]
        
    @rx.var
    def phase_data(self) -> Dict[str, Any]:
        return LESSON_1_1["steps"].get(self.current_phase_key, {})
        
    @rx.var
    def progress_percent(self) -> int:
        return int((self.current_phase_index / (len(PHASES) - 1)) * 100)
        
    @rx.var
    def can_advance(self) -> bool:
        phase_type = self.phase_data.get("type", "text")
        if phase_type == "text":
            return True
        return self.is_success
        
    async def load_lesson(self):
        target_phase = 0
        
        auth = await self.get_state(AuthState)
        
        # Handle race condition where AuthState.on_load hasn't finished yet
        if not auth.is_authenticated and auth.auth_token:
            from SKILLOGIC.lib.supabase_client import get_supabase
            client = get_supabase()
            if client:
                try:
                    res = client.auth.get_user(auth.auth_token)
                    if res and res.user:
                        auth.user_id = res.user.id
                except Exception:
                    pass

        if auth.is_authenticated:
            profile = fetch_user_profile(auth.user_id)
            if profile:
                prog = profile.get("progress") or {}
                lessons = prog.get("lessons", {})
                lesson_data = lessons.get(self.lesson_id)
                if lesson_data and lesson_data.get("status") == "in_progress":
                    target_phase = lesson_data.get("phase", 0)
        
        self.current_phase_index = target_phase
        self.setup_phase()
        
    async def _save_current_progress_to_db(self, completed: bool = False):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return
            
        profile = fetch_user_profile(auth.user_id)
        if not profile:
            return
            
        prog = profile.get("progress") or {}
        lessons = prog.get("lessons", {})
        
        lessons[self.lesson_id] = {
            "status": "completed" if completed else "in_progress",
            "phase": self.current_phase_index
        }
        
        prog["lessons"] = lessons
        update_user_progress(auth.user_id, prog)

    async def save_and_exit(self):
        await self._save_current_progress_to_db(completed=False)
        return rx.redirect("/dashboard")
        
    async def finish_lesson(self):
        await self._save_current_progress_to_db(completed=True)
        return rx.redirect("/dashboard")
        
    def setup_phase(self):
        """Initializes the UI state based on the current phase type."""
        self.terminal_output = ""
        self.is_success = False
        self.feedback_message = ""
        self.show_pro_feedback = False
        
        data = self.phase_data
        phase_type = data.get("type")
        
        if phase_type == "code":
            self.user_code = data.get("starter_code", "")
        elif phase_type == "parsons":
            self.parsons_blocks = data.get("blocks", [])
            self.user_order = []
        else:
            self.user_code = ""

    def set_user_code(self, val: str):
        self.user_code = val
        
    def set_user_order(self, order: List[str]):
        """For Drag & Drop Parsons problem."""
        self.user_order = order
        
    def move_block_up(self, block_id: str):
        blocks = self.parsons_blocks
        for i, b in enumerate(blocks):
            if b["id"] == block_id and i > 0:
                blocks[i], blocks[i-1] = blocks[i-1], blocks[i]
                self.parsons_blocks = blocks
                break

    def move_block_down(self, block_id: str):
        blocks = self.parsons_blocks
        for i, b in enumerate(blocks):
            if b["id"] == block_id and i < len(blocks) - 1:
                blocks[i], blocks[i+1] = blocks[i+1], blocks[i]
                self.parsons_blocks = blocks
                break
        
    def next_phase(self):
        if self.current_phase_index < len(PHASES) - 1:
            self.current_phase_index += 1
            self.setup_phase()
            
    def prev_phase(self):
        if self.current_phase_index > 0:
            self.current_phase_index -= 1
            self.setup_phase()
            
    def toggle_pro_feedback(self):
        self.show_pro_feedback = not self.show_pro_feedback
            
    def check_parsons(self):
        correct = self.phase_data.get("correct_order", [])
        current_order = [b["id"] for b in self.parsons_blocks]
        if current_order == correct:
            self.is_success = True
            self.feedback_message = "¡Correcto! " + self.phase_data.get("explanation", "")
        else:
            self.is_success = False
            self.feedback_message = "Aún no. Piensa en el orden lógico: primero pides, luego guardas, luego operas, y al final muestras."

    def run_code(self):
        """Executes the Python code locally and captures stdout and errors."""
        self.terminal_output = ""
        self.is_success = False
        self.feedback_message = ""
        
        if not self.user_code.strip():
            self.terminal_output = "No hay código para ejecutar."
            return

        # Prepare capture
        f = io.StringIO()
        
        # NOTE: Using exec() directly for the local MVP.
        # In a real production app, this MUST be sent to a secure sandbox (like Docker or WebAssembly/Pyodide).
        try:
            with contextlib.redirect_stdout(f):
                # We need a clean namespace
                namespace = {}
                
                # Mock input() so it doesn't block forever in the backend
                # For this MVP, we will inject a fake input() that returns a default value 
                # or the required input for validation.
                inputs_to_mock = []
                val_data = self.phase_data.get("validation", {})
                if val_data and val_data.get("inputs"):
                    inputs_to_mock = val_data["inputs"][0].copy() # Get first test case inputs
                
                def mock_input(prompt=""):
                    print(prompt, end="")
                    if inputs_to_mock:
                        val = inputs_to_mock.pop(0)
                        print(val) # Echo the input
                        return val
                    print("TEST_INPUT")
                    return "TEST_INPUT"
                    
                namespace['input'] = mock_input
                
                exec(self.user_code, namespace)
                
            output = f.getvalue()
            self.terminal_output = output
            
            # Validate output if validation data exists
            if val_data and val_data.get("expected_outputs"):
                expected = val_data["expected_outputs"][0]
                if expected.lower() in output.lower():
                    self.is_success = True
                    self.feedback_message = "¡Perfecto! Has completado el desafío."
                else:
                    self.is_success = False
                    self.feedback_message = f"Casi. Se esperaba que el resultado incluyera: '{expected}'"
            else:
                # If no validation required, just running it successfully is a pass
                self.is_success = True
                self.feedback_message = "Código ejecutado sin errores."

        except Exception as e:
            # Capture the raw traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            # Get the exact error line
            tb_list = traceback.format_exception(exc_type, exc_value, exc_traceback)
            
            # We want to filter out the exec() parts and show the actual error to the user
            raw_error = "".join(tb_list[-2:])
            self.terminal_output = f.getvalue() + "\n" + raw_error
            self.is_success = False
            
            # Check for Pedagogical Feedback mapping (Step 6)
            error_name = type(e).__name__
            feedback_mapping = LESSON_1_1["steps"].get("6_feedback", {}).get("errors", [])
            for mapping in feedback_mapping:
                if mapping["error_type"] == error_name:
                    # We found a matching pedagogical feedback
                    self.feedback_message = mapping["free"]  # Default to free
                    # Note: UI will show a button to switch to PRO feedback (mapping["pro"])
                    # We'll store the pro message temporarily in state if needed, but we can just compute it in UI
                    break
            
            if not self.feedback_message:
                self.feedback_message = f"Error: {error_name}. Revisa tu código."
