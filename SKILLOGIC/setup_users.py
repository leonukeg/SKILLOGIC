import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

c = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_ANON_KEY'))

users = [
    {"email": "admin@skillogic.com", "password": "admin123", "log": "admin"},
    {"email": "chemaruan@gmail.com", "password": "19001256", "log": "leonukeg"}
]

for u in users:
    print(f"Configuring {u['log']}...")
    try:
        # Intentar crear
        res = c.auth.sign_up({
            "email": u["email"],
            "password": u["password"],
            "options": {"data": {"full_name": u["log"]}}
        })
        user_id = res.user.id
        print(" -> Creado nuevo.")
    except Exception as e:
        # Si existe, loguear
        try:
            res = c.auth.sign_in_with_password({"email": u["email"], "password": u["password"]})
            user_id = res.user.id
            print(" -> Logueado existente.")
        except Exception as e2:
            print(f" -> Error con {u['log']}: {e2}")
            continue

    # Wipe progress and set role to master, and save email
    # Primero buscamos si existe perfil
    p_res = c.table('profiles').select('*').eq('id', user_id).execute()
    
    new_progress = {"role": "master", "lessons": {}}
    
    if p_res.data and len(p_res.data) > 0:
        c.table('profiles').update({
            "progress": new_progress,
            "email": u["email"],
            "xp": 0,
            "streak": 0
        }).eq('id', user_id).execute()
        print(" -> Perfil reseteado.")
    else:
        c.table('profiles').insert({
            "id": user_id,
            "progress": new_progress,
            "email": u["email"],
            "xp": 0,
            "streak": 0
        }).execute()
        print(" -> Perfil creado.")

print("Listo!")
