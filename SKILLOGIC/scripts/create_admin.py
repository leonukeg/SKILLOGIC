import os
from dotenv import load_dotenv
load_dotenv()
from SKILLOGIC.lib.supabase_client import get_supabase

def create_admin():
    client = get_supabase()
    try:
        res = client.auth.sign_up({
            "email": "admin@skillogic.com",
            "password": "admin123",
            "options": {"data": {"full_name": "Administrador"}}
        })
        print("Admin creado:", res.user.email)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    create_admin()
