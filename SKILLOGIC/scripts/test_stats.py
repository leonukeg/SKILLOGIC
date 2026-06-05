from SKILLOGIC.lib.supabase_client import get_supabase

client = get_supabase()
users = client.table("user_stats").select("*").execute()
print(users.data)
