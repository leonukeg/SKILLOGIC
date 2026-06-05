import os
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

sql_script = """
create table if not exists public.profiles (
  id uuid references auth.users on delete cascade primary key,
  email text,
  progress jsonb default '{}'::jsonb,
  streak integer default 0,
  xp integer default 0,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Asegurar que RLS (Row Level Security) protege los datos
alter table public.profiles enable row level security;
drop policy if exists "Usuarios pueden ver su propio perfil." on public.profiles;
create policy "Usuarios pueden ver su propio perfil." on public.profiles for select using (auth.uid() = id);

drop policy if exists "Usuarios pueden actualizar su perfil." on public.profiles;
create policy "Usuarios pueden actualizar su perfil." on public.profiles for update using (auth.uid() = id);

drop policy if exists "Usuarios pueden insertar su perfil." on public.profiles;
create policy "Usuarios pueden insertar su perfil." on public.profiles for insert with check (auth.uid() = id);
"""

def setup_db():
    if not DATABASE_URL:
        print("No DATABASE_URL found in .env")
        return
        
    engine = sqlalchemy.create_engine(DATABASE_URL)
    with engine.connect() as conn:
        conn.execute(sqlalchemy.text(sql_script))
        conn.commit()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_db()
