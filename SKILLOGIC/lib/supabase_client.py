import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# Initialize the client from environment variables
url: str = os.getenv("SUPABASE_URL", "")
key: str = os.getenv("SUPABASE_ANON_KEY", "")

# We only create the client if the URL and KEY are present
if url and key and key != "AQUI_VA_TU_CLAVE_ANONIMA":
    supabase: Client = create_client(url, key)
else:
    supabase = None

def get_supabase() -> Client:
    """Returns the supabase client instance."""
    if not supabase:
        print("WARNING: Supabase no está configurado correctamente en el .env.")
    return supabase

def fetch_user_profile(user_id: str) -> dict:
    """Obtiene el perfil del usuario (incluyendo el progreso)."""
    client = get_supabase()
    if not client: return {}
    
    response = client.table("profiles").select("*").eq("id", user_id).execute()
    if response.data and len(response.data) > 0:
        return response.data[0]
        
    # Auto-create if it doesn't exist
    try:
        new_profile = {
            "id": user_id,
            "progress": {},
            "streak": 0,
            "xp": 0
        }
        client.table("profiles").insert(new_profile).execute()
        return new_profile
    except Exception as e:
        print("Error auto-creating profile:", e)
        
    return {}

def update_user_progress(user_id: str, progress_data: dict):
    """Actualiza la columna progress (JSONB) en la tabla profiles."""
    client = get_supabase()
    if not client: return
    
    client.table("profiles").update({"progress": progress_data}).eq("id", user_id).execute()

def fetch_user_stats(user_id: str) -> dict:
    """Obtiene las estadísticas de gamificación del usuario."""
    client = get_supabase()
    if not client: return {}
    
    response = client.table("user_stats").select("*").eq("user_id", user_id).execute()
    if response.data and len(response.data) > 0:
        return response.data[0]
    return {}

def update_user_stats(user_id: str, stats_data: dict):
    """Actualiza las estadísticas de gamificación en la tabla user_stats."""
    client = get_supabase()
    if not client: return
    
    client.table("user_stats").update(stats_data).eq("user_id", user_id).execute()
