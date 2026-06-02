import os
import re

dashboard_path = r"c:\Users\Freddy\Desktop\Cosas_Python\SKILLOGIC\SKILLOGIC\pages\dashboard.py"
out_dir = r"c:\Users\Freddy\Desktop\Cosas_Python\SKILLOGIC\SKILLOGIC\components\dashboard"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

imports = """import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.state.curriculum_state import CurriculumState
from SKILLOGIC.state.progress_state import ProgressState
"""

file_map = {
    "_hero_card": "hero.py",
    "_learning_path": "learning_path.py",
    "_daily_challenge": "daily_challenge.py",
    "_todays_plan": "todays_plan.py",
    "_stats_overview": "stats.py",
    "_recent_projects": "recent_projects.py",
}

# The _right_panel uses many of these, we should leave it in dashboard.py or extract it too.
# Let's extract it as well.
file_map["_right_panel"] = "right_panel.py"

new_dashboard_content = """import reflex as rx
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.state.curriculum_state import CurriculumState
from SKILLOGIC.state.progress_state import ProgressState
from SKILLOGIC.components.layout import app_layout
from SKILLOGIC.styles import theme as T

# Decorative accents — same across themes
_VIOLET = "#a855f7"
_LILAC  = "#a78bfa"

"""

for func, filename in file_map.items():
    pattern = rf"(def {func}\(.*?)(?=def \w|\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        func_content = match.group(1)
        
        # If it's right_panel, we need to import the others inside it or above it
        extra_imports = ""
        if func == "_right_panel":
            extra_imports = "from SKILLOGIC.components.dashboard.daily_challenge import _daily_challenge\nfrom SKILLOGIC.components.dashboard.todays_plan import _todays_plan\nfrom SKILLOGIC.components.dashboard.stats import _stats_overview\nfrom SKILLOGIC.components.dashboard.recent_projects import _recent_projects\n"
            
        with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
            f.write(imports + extra_imports + "\n" + func_content)
        new_dashboard_content += f"from SKILLOGIC.components.dashboard.{filename[:-3]} import {func}\n"

# Add the main dashboard function
lp_match = re.search(r'(def dashboard_page\(\) -> rx\.Component:.*?)\Z', content, re.DOTALL)
if lp_match:
    new_dashboard_content += "\n" + lp_match.group(1)

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(new_dashboard_content)

print("Dashboard refactor complete!")
