# ⚡ SKILLOGIC

> **"De la teoría aburrida a la programación real."**

SKILLOGIC es la cura definitiva contra el "Infierno de los Tutoriales". Es una plataforma interactiva, gamificada y de alta intensidad diseñada para enseñarte Python a través de la **práctica activa**. Olvídate de ver horas de videos sin escribir una sola línea de código; aquí el 90% del tiempo estarás programando y el 10% aprendiendo teoría.

Construida con [Reflex](https://reflex.dev) (Python puro Full-Stack), integrando **PostgreSQL** y metodologías probadas en entrevistas técnicas de las principales empresas de tecnología (FAANG).

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| **Frontend & Backend** | Reflex (Pure Python) |
| **Base de Datos** | Supabase (PostgreSQL) + Row Level Security |
| **Autenticación** | Supabase GoTrue (Email & Password) |
| **UI/UX** | Atomic Vibe Design, Flexbox, Tokens Centralizados |

## 🔥 Características Principales

### 🧠 Práctica Activa e Inmersiva
- **Consola de Python en el Navegador**: Ejecuta código Python real en milisegundos directamente en la interfaz. Sin instalar nada.
- **Katas de Dificultad Real (FAANG)**: Contamos con una base de datos dinámica de **100 Katas progresivos** repartidos por lección. Tienen una "dificultad engañosa". Lo que parece fácil, en realidad te obligará a exprimir tu lógica matemática. Los niveles difíciles incluyen problemas reales de FAANG.
- **Evaluador Invisible**: Tus scripts se evalúan en tiempo real contra pruebas unitarias (`asserts`) completamente ocultas.

### 🎮 Gamificación Adictiva (Dopamine Hacking)
- **Rachas (Streaks)**: Mantén el fuego vivo. Si programas a diario, ganas multiplicadores de XP.
- **Experiencia y Rangos**: Sube de "Novato" a "Master" resolviendo lecciones y Katas.
- **Popups de Logros Cyberpunk**: Retroalimentación visual inmediata inspirada en el "Snake Game" cada vez que resuelves un reto.

### 🎨 Diseño y UX Premium (Atomic Vibe)
- **Modo Oscuro/Claro Nativo**.
- **Renderizado Adaptativo (Responsive)**: Perfectamente usable desde un celular en el metro o en un monitor 4K.
- **Landing Page Optimizada**: Con enfoque en conversiones mediante estrategias P.A.S. y F.A.B.

---

## 🏗️ Estructura del Proyecto

```text
SKILLOGIC/
├── SKILLOGIC/
│   ├── SKILLOGIC.py       # App Root: Rutas, Global Styles y Configuración
│   ├── styles/            # Theme Tokens: Colores y espaciados centralizados
│   ├── state/             # Local States: auth_state, progress_state, kata_state
│   ├── components/        # UI Reutilizable: navbar, footer, gamification_popup
│   ├── data/              # Base de datos estática: Lecciones y Katas
│   └── pages/             # Vistas: landing, about, dashboard, katas, etc.
├── rxconfig.py            # Configuración de Reflex
└── requirements.txt       # Dependencias
```

---

## 🚀 Setup Local Rápido

1. **Clonar y crear el entorno virtual**:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Variables de Entorno (`.env`)**:
   Crea un archivo `.env` en la raíz con tus llaves de Supabase:
   ```env
   SUPABASE_URL="tu_supabase_url"
   SUPABASE_KEY="tu_anon_key"
   SUPABASE_SERVICE_ROLE_KEY="tu_secret_key" # Requerido para funciones Admin
   ```

4. **Levantar la plataforma**:
   ```bash
   reflex run
   ```

---

## 🗺️ Roadmap de Desarrollo
- [x] Consola interactiva integrada.
- [x] Gamificación (XP y Rachas).
- [x] Base de datos de 100 Katas progresivos nivel Entrevista integrados.
- [x] Currículum ampliado a más del 50% de contenido inicial (Módulos 1 y 2 completos).
- [ ] Ejecución en entorno aislado Sandbox / Dockerización de respuestas.
- [ ] Tablas de clasificación (Leaderboard Global).

---
*Made with ⚡ and lots of code by SKILLOGIC.*
