# ⚡ SKILLOGIC

> **"La programación se aprende programando."**

Plataforma de aprendizaje de Python construida en **Reflex** — Python puro, sin cambiar de lenguaje.

## Stack

| Capa | Tecnología |
|------|-----------|
| Frontend + Backend | [Reflex](https://reflex.dev) (Python) |
| Base de datos | SQLite (dev) → PostgreSQL/Supabase (prod) |
| Deploy | Railway |

## Estructura del proyecto

```
SKILLOGIC/
├── SKILLOGIC/
│   ├── SKILLOGIC.py       # Entry point (rx.App)
│   ├── styles/
│   │   └── theme.py       # Design tokens (colores, tipografía, spacing)
│   ├── state/
│   │   └── app_state.py   # AppState(rx.State) — auth, tema, idioma
│   ├── components/
│   │   ├── sidebar.py     # Sidebar con progreso y racha
│   │   ├── topbar.py      # Topbar con toggle tema/idioma
│   │   └── layout.py      # app_layout() wrapper
│   └── pages/
│       ├── login.py       # Página de login
│       └── dashboard.py   # Dashboard principal
├── prototype/             # Referencia visual HTML/CSS/JS
├── rxconfig.py
└── requirements.txt
```

## Setup

```bash
# 1. Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# 2. Instalar dependencias
pip install reflex

# 3. Arrancar en desarrollo
reflex run
```

App en `http://localhost:3000` · Backend en `http://localhost:8000`

## Características (Phase 0 — MVP)

- 🌙 / ☀️ **Modo oscuro / claro** — un toggle cambia ambos simultáneamente
- 🇪🇸 / 🇬🇧 **Español / English** — vinculado al tema (dark=ES, light=EN)
- 🔥 **Racha diaria** — calendario semanal en el sidebar
- 📊 **Barra de XP** — progreso de nivel visual
- 🗺️ **Ruta de aprendizaje** — módulos con barra de progreso
- ⌨️ **Preview de editor** — código estático en el dashboard

## Roadmap

- [ ] Phase 1 — Backend FastAPI + SQLAlchemy + Supabase
- [ ] Phase 2 — Monaco Editor + ejecución de código (RestrictedPython)
- [ ] Phase 3 — Gamificación completa (XP, logros, leaderboard)
- [ ] Phase 4 — Comunidad + proyectos colaborativos
- [ ] Phase 5 — Deploy Railway + PWA

---

Made with ⚡ by **SKILLOGIC**
