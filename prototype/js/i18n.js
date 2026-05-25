/* ================================================================
   SKILLOGIC — i18n (Internationalization)
   Pure data: no UI logic, no side effects.
   Primary language: Spanish (es). Secondary: English (en).
   Usage: I18n.t('key') or the global shorthand t('key')
   ================================================================ */

'use strict';

const I18N_STRINGS = {

  /* ── Spanish (primary) ──────────────────────────────────────── */
  es: {
    /* Navigation */
    nav_home:          'Inicio',
    nav_learning_path: 'Ruta de Aprendizaje',
    nav_lessons:       'Lecciones',
    nav_projects:      'Proyectos',
    nav_challenges:    'Desafíos',
    nav_code_lab:      'Code Lab',
    nav_community:     'Comunidad',
    nav_resources:     'Recursos',

    /* Sidebar sections */
    sidebar_progress:       'Tu Progreso',
    sidebar_streak:         'Racha Actual',
    sidebar_rank:           'Rango',
    sidebar_next_obj:       'Próximo objetivo',
    sidebar_help:           '¿Necesitas ayuda?',
    sidebar_community_join: 'Únete a nuestra comunidad',
    sidebar_community_btn:  'Ir a la comunidad →',

    /* Days */
    days_short: ['L','M','M','J','V','S','D'],
    days_label: 'días',

    /* Hero */
    hero_title:       'Aprende Python.',
    hero_accent:      'Construye el futuro. 🚀',
    hero_description: 'Un camino práctico, moderno y efectivo para llevar tus habilidades de Python al siguiente nivel.',
    hero_cta_primary: '▶ Continuar aprendiendo',
    hero_cta_secondary:'Ver mi ruta',

    /* Learning path */
    learning_path_title: 'Tu ruta de aprendizaje',
    learning_path_link:  'Ver ruta completa →',

    /* Current lesson */
    current_lesson_label: 'Lección actual',
    open_lesson:          'Abrir lección',
    tab_instructions:     '📖 Instrucciones',
    tab_hint:             '💡 Pista',
    tab_discussion:       '💬 Discusión',
    run_btn:              '▶ Ejecutar',
    run_btn_loading:      '⏳',
    reset_btn:            '⟳ Reiniciar',
    hint_btn:             '💡 Pista',
    execute_run:          '▶ Ejecutar',

    /* Output panel */
    output_label:    'Salida',
    clear_output:    'Limpiar',
    tests_label:     'Tests',
    output_empty:    'Ejecuta el código para ver la salida',

    /* Python status */
    python_loading:  'Cargando Python... (primera vez puede tardar unos segundos)',
    python_ready:    'Python listo ✓',

    /* Run status */
    run_running:     'Ejecutando...',
    run_success:     '¡Correcto! +{xp} XP 🎉',
    run_error:       'Algunos tests fallaron. ¡Sigue intentando!',
    run_unexpected:  'Error inesperado al ejecutar',

    /* Right panel */
    streak_widget_title: 'Racha actual 🔥',
    streak_keep_going:   '¡Sigue así! 👋',
    plan_today_title:    'Plan de hoy',
    plan_see_all:        'Ver todo',
    plan_continue_btn:   'Continuar plan',
    challenge_title:     'Desafío diario',
    challenge_new:       'Nuevo',
    challenge_difficulty:'Dificultad',
    challenge_easy:      'Fácil',
    challenge_name:      'Suma de números pares',
    challenge_desc:      'Crea una función que reciba un número n y devuelva la suma de todos los números pares hasta n.',
    challenge_btn:       '▶ Resolver desafío',
    challenge_see_all:   'Ver todos los desafíos →',
    community_title:     'Comunidad activa',
    community_btn:       'Ir a la comunidad →',

    /* Projects */
    projects_title:   'Proyectos para ti',
    projects_see_all: 'Ver todos →',
    proj_names: ['Generador de Contraseñas', 'Web Scraper', 'Lista de Tareas', 'Análisis de Datos'],

    /* Lesson page */
    back_dashboard:    '← Dashboard',
    lesson_exercises:  'Ejercicios',
    hint_label:        'Pista',

    /* Today plan items */
    plan_items: [
      { title: 'Funciones en Python', sub: 'Lección 5' },
      { title: 'Desafío: Calculadora', sub: 'Intermedio' },
      { title: 'Proyecto: Habit Tracker', sub: 'Práctico' },
    ],

    /* Community feed */
    community_feed: [
      { msg: 'María completó el proyecto Habit Tracker 🎉', time: 'hace 2h' },
      { msg: 'Juan respondió en "List comprehensions"',      time: 'hace 3h' },
      { msg: 'PythonLover14 logró una racha de 30 días 🔥', time: 'hace 5h' },
    ],

    /* Module names */
    module_names: [
      'Fundamentos Reales',
      'Estructuras de Datos',
      'Funciones y Módulos',
      'POO',
      'Proyectos',
    ],

    /* Auth — Login */
    login_title:         'Bienvenido de vuelta',
    login_subtitle:      'Continúa aprendiendo Python donde lo dejaste',
    login_email_label:   'Correo electrónico',
    login_email_ph:      'tu@email.com',
    login_pwd_label:     'Contraseña',
    login_pwd_ph:        '••••••••',
    login_btn:           'Iniciar sesión',
    login_btn_loading:   'Iniciando sesión...',
    login_demo_btn:      '🚀 Entrar con cuenta demo',
    login_or:            'o',
    login_no_account:    '¿No tienes cuenta?',
    login_register_link: 'Regístrate gratis',

    /* Auth — Register */
    register_title:       'Empieza a programar',
    register_subtitle:    'Gratis para siempre. Sin tarjeta de crédito.',
    register_name_label:  'Tu nombre',
    register_name_ph:     'Ana García',
    register_email_label: 'Correo electrónico',
    register_email_ph:    'tu@email.com',
    register_pwd_label:   'Contraseña',
    register_pwd_ph:      'Mínimo 8 caracteres',
    register_terms:       'Al registrarte aceptas nuestros',
    register_terms_link:  'Términos de uso',
    register_and:         'y',
    register_privacy:     'Política de privacidad',
    register_btn:         'Crear cuenta gratis',
    register_btn_loading: 'Creando cuenta...',
    register_has_account: '¿Ya tienes cuenta?',
    register_login_link:  'Iniciar sesión',

    /* Password strength */
    pwd_too_short: 'Demasiado corta',
    pwd_weak:      'Débil',
    pwd_fair:      'Regular',
    pwd_good:      'Buena',
    pwd_excellent: '¡Excelente!',

    /* Validation errors */
    err_fill_fields:  'Por favor, completa todos los campos.',
    err_pwd_short:    'La contraseña debe tener al menos 8 caracteres.',

    /* Toasts */
    toast_welcome: '¡Bienvenido a SKILLOGIC! 🚀',
    toast_xp:      '¡Ejercicio completado! +{xp} XP 🎉',

    /* Topbar */
    search_placeholder: 'Buscar lecciones, temas o desafíos...',
    logout_confirm:     '¿Cerrar sesión?',
    notifications:      'Notificaciones',

    /* Toggle label */
    toggle_label: '🌙 ES',
    toggle_title: 'Cambiar a modo claro / inglés',

    /* Difficulty labels */
    diff_basic:        'Básico',
    diff_intermediate: 'Intermedio',
    diff_advanced:     'Avanzado',
  },

  /* ── English (secondary) ────────────────────────────────────── */
  en: {
    /* Navigation */
    nav_home:          'Home',
    nav_learning_path: 'Learning Path',
    nav_lessons:       'Lessons',
    nav_projects:      'Projects',
    nav_challenges:    'Challenges',
    nav_code_lab:      'Code Lab',
    nav_community:     'Community',
    nav_resources:     'Resources',

    /* Sidebar sections */
    sidebar_progress:       'Your Progress',
    sidebar_streak:         'Current Streak',
    sidebar_rank:           'Rank',
    sidebar_next_obj:       'Next objective',
    sidebar_help:           'Need help?',
    sidebar_community_join: 'Join our community',
    sidebar_community_btn:  'Go to community →',

    /* Days */
    days_short: ['M','T','W','T','F','S','S'],
    days_label: 'days',

    /* Hero */
    hero_title:        'Learn Python.',
    hero_accent:       'Build the future. 🚀',
    hero_description:  'A practical, modern and effective path to take your Python skills to the next level.',
    hero_cta_primary:  '▶ Continue learning',
    hero_cta_secondary:'View my path',

    /* Learning path */
    learning_path_title: 'Your learning path',
    learning_path_link:  'View full path →',

    /* Current lesson */
    current_lesson_label: 'Current lesson',
    open_lesson:          'Open lesson',
    tab_instructions:     '📖 Instructions',
    tab_hint:             '💡 Hint',
    tab_discussion:       '💬 Discussion',
    run_btn:              '▶ Run',
    run_btn_loading:      '⏳',
    reset_btn:            '⟳ Reset',
    hint_btn:             '💡 Hint',
    execute_run:          '▶ Run',

    /* Output panel */
    output_label:    'Output',
    clear_output:    'Clear',
    tests_label:     'Tests',
    output_empty:    'Run the code to see the output',

    /* Python status */
    python_loading:  'Loading Python... (first time may take a few seconds)',
    python_ready:    'Python ready ✓',

    /* Run status */
    run_running:     'Running...',
    run_success:     'Correct! +{xp} XP 🎉',
    run_error:       'Some tests failed. Keep trying!',
    run_unexpected:  'Unexpected error during execution',

    /* Right panel */
    streak_widget_title: 'Current streak 🔥',
    streak_keep_going:   'Keep it up! 👋',
    plan_today_title:    "Today's plan",
    plan_see_all:        'See all',
    plan_continue_btn:   'Continue plan',
    challenge_title:     'Daily challenge',
    challenge_new:       'New',
    challenge_difficulty:'Difficulty',
    challenge_easy:      'Easy',
    challenge_name:      'Sum of even numbers',
    challenge_desc:      'Create a function that receives a number n and returns the sum of all even numbers up to n.',
    challenge_btn:       '▶ Solve challenge',
    challenge_see_all:   'See all challenges →',
    community_title:     'Active community',
    community_btn:       'Go to community →',

    /* Projects */
    projects_title:   'Projects for you',
    projects_see_all: 'See all →',
    proj_names: ['Password Generator', 'Web Scraper', 'Task List', 'Data Analysis'],

    /* Lesson page */
    back_dashboard:    '← Dashboard',
    lesson_exercises:  'Exercises',
    hint_label:        'Hint',

    /* Today plan items */
    plan_items: [
      { title: 'Functions in Python', sub: 'Lesson 5' },
      { title: 'Challenge: Calculator', sub: 'Intermediate' },
      { title: 'Project: Habit Tracker', sub: 'Practical' },
    ],

    /* Community feed */
    community_feed: [
      { msg: 'María completed the Habit Tracker project 🎉', time: '2h ago' },
      { msg: 'Juan replied in "List comprehensions"',          time: '3h ago' },
      { msg: 'PythonLover14 reached a 30-day streak 🔥',      time: '5h ago' },
    ],

    /* Module names */
    module_names: [
      'Real Fundamentals',
      'Data Structures',
      'Functions & Modules',
      'OOP',
      'Projects',
    ],

    /* Auth — Login */
    login_title:         'Welcome back',
    login_subtitle:      'Continue learning Python where you left off',
    login_email_label:   'Email address',
    login_email_ph:      'you@email.com',
    login_pwd_label:     'Password',
    login_pwd_ph:        '••••••••',
    login_btn:           'Sign in',
    login_btn_loading:   'Signing in...',
    login_demo_btn:      '🚀 Enter with demo account',
    login_or:            'or',
    login_no_account:    "Don't have an account?",
    login_register_link: 'Sign up for free',

    /* Auth — Register */
    register_title:       'Start programming',
    register_subtitle:    'Free forever. No credit card.',
    register_name_label:  'Your name',
    register_name_ph:     'Ana García',
    register_email_label: 'Email address',
    register_email_ph:    'you@email.com',
    register_pwd_label:   'Password',
    register_pwd_ph:      'At least 8 characters',
    register_terms:       'By signing up you agree to our',
    register_terms_link:  'Terms of use',
    register_and:         'and',
    register_privacy:     'Privacy policy',
    register_btn:         'Create free account',
    register_btn_loading: 'Creating account...',
    register_has_account: 'Already have an account?',
    register_login_link:  'Sign in',

    /* Password strength */
    pwd_too_short: 'Too short',
    pwd_weak:      'Weak',
    pwd_fair:      'Fair',
    pwd_good:      'Good',
    pwd_excellent: 'Excellent!',

    /* Validation errors */
    err_fill_fields: 'Please fill in all fields.',
    err_pwd_short:   'Password must be at least 8 characters.',

    /* Toasts */
    toast_welcome: 'Welcome to SKILLOGIC! 🚀',
    toast_xp:      'Exercise completed! +{xp} XP 🎉',

    /* Topbar */
    search_placeholder: 'Search lessons, topics or challenges...',
    logout_confirm:     'Sign out?',
    notifications:      'Notifications',

    /* Toggle label */
    toggle_label: '☀️ EN',
    toggle_title: 'Switch to dark mode / Spanish',

    /* Difficulty labels */
    diff_basic:        'Basic',
    diff_intermediate: 'Intermediate',
    diff_advanced:     'Advanced',
  },
};

/* ================================================================
   I18n service — singleton
   ================================================================ */
const I18n = (() => {
  let _lang = 'es';

  return {
    setLang(lang) {
      _lang = (lang === 'en') ? 'en' : 'es';
    },

    getLang() { return _lang; },

    /**
     * Translate a key, optionally replacing {placeholder} tokens.
     * Falls back to ES if EN key is missing, then to the raw key.
     */
    t(key, params = {}) {
      const dict = I18N_STRINGS[_lang] || I18N_STRINGS.es;
      let str = dict[key];

      /* Fallback to ES */
      if (str === undefined) str = I18N_STRINGS.es[key];

      /* Last resort: return the key itself */
      if (str === undefined) {
        console.warn(`[I18n] Missing key: "${key}" in lang "${_lang}"`);
        return key;
      }

      /* Skip template substitution for non-strings */
      if (typeof str !== 'string') return str;

      Object.keys(params).forEach(k => {
        str = str.replace(`{${k}}`, params[k]);
      });

      return str;
    },

    /* Convenience: get an array value */
    arr(key) {
      const dict = I18N_STRINGS[_lang] || I18N_STRINGS.es;
      return dict[key] || I18N_STRINGS.es[key] || [];
    },
  };
})();

/* Global shorthand — used throughout page templates */
function t(key, params) { return I18n.t(key, params); }
