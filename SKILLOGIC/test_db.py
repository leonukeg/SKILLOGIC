import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()

# 1. Add role column
cur.execute("ALTER TABLE profiles ADD COLUMN IF NOT EXISTS role VARCHAR(50) DEFAULT 'basic';")

# 2. Query all users
cur.execute("""
    SELECT u.id, u.email, p.role, p.progress
    FROM auth.users u
    LEFT JOIN public.profiles p ON u.id = p.id;
""")
users = cur.fetchall()
print(users)

conn.commit()
cur.close()
conn.close()
