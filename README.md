# ⚡ SKILLOGIC

> **"La programación se aprende programando."**

Plataforma de aprendizaje de Python construida en **Reflex** — Python puro, sin cambiar de lenguaje. Desarrollado con una metodología pedagógica inmersiva.

## Stack

| Capa | Tecnología |
|------|-----------|
| Frontend + Backend | [Reflex](https://reflex.dev) (Python) |
| Base de datos | Supabase (PostgreSQL) + Gotrue Auth |
| UI/UX | Diseño Atómico, Flexbox Responsivo, Tokens de Diseño (Theme) |

## Características Actuales (MVP Funcional)

- 🌙 / ☀️ **Modo oscuro / claro** — Soporte nativo para cambio de tema y tokens de diseño avanzados.
- 📱 **Totalmente Responsivo** — UI adaptada para móviles, tablets y escritorio (Flex wrap, Stack vertical en móvil).
- 🔐 **Autenticación Completa (Supabase)** — Registro, Login y Recuperación de contraseña completamente integrados.
- 🎓 **Lecciones Interactivas (Metodología SKILLOGIC)**:
  - Fases progresivas (Hook, Parsons, Theory, Guided Build, Struggle, Retrieval).
  - Problemas de Parsons interactivos (puzzle lógico).
  - Feedback Pedagógico PRO (Simulación de IA) para errores tipificados.
  - Editor de código y terminal integrados.
- 🥋 **Dojo de Katas** — Desafíos de programación clasificados por dificultad con recompensas de XP.
- 📊 **Dashboard & Progreso** — Barra de XP, sistema de rangos, conteo de rachas (Streaks) y katas resueltos guardados en base de datos.
- 🗺️ **Roadmap Dinámico** — Ruta de aprendizaje visual interactiva.

## Estructura del proyecto

```
SKILLOGIC/
├── SKILLOGIC/
│   ├── SKILLOGIC.py       # Entry point (rx.App) y Configuración Supabase
│   ├── styles/            # Design tokens (colores, tipografía, spacing)
│   ├── state/             # Gestión de estado separado por dominio (auth, app, lesson, progress)
│   ├── components/        # Componentes UI reutilizables (landing, layout, auth)
│   ├── data/              # Base de datos local (Katas, contenido de lecciones)
│   └── pages/             # Vistas principales (dashboard, lesson, katas, login, etc.)
├── rxconfig.py
└── requirements.txt
```

## Setup Local

```bash
# 1. Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Variables de entorno (.env)
SUPABASE_URL="tu_supabase_url"
SUPABASE_KEY="tu_anon_key"

# 4. Arrancar en desarrollo
reflex run
```

## Próximos Pasos (Roadmap)
- [ ] Ejecución de código segura en Backend (RestrictedPython / Pyodide)
- [ ] Leaderboard Global y Sistema de Logros
- [ ] Deploy a Producción (Railway / Vercel)

---

Made with ⚡ by **SKILLOGIC**
