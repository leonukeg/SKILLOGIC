/* ================================================================
   SKILLOGIC — State Management
   Immutable-by-default mock state.
   All mutations go through explicit setters to preserve traceability.
   ================================================================ */

'use strict';

const AppState = (() => {
  /* ── Private state ─────────────────────────────────────────── */
  let _state = {
    /* Auth */
    isAuthenticated: false,
    currentUser: null,

    /* Current navigation */
    currentRoute:   null,
    currentLesson:  null,   // full lesson object
    currentExercise: null,  // exercise object within the lesson

    /* Runtime */
    pythonReady:    false,  // Pyodide loaded flag
    monacoReady:    false,

    /* User progress (persisted in localStorage) */
    userProgress: {},       // { [lessonSlug]: { completedExercises: [], xpEarned: 0 } }
  };

  /* ── Mock user data ─────────────────────────────────────────── */
  const MOCK_USER = {
    id:         'usr_001',
    name:       'Juan',
    email:      'juan@example.com',
    level:      4,
    xp:         820,
    xpToNext:   1200,
    streak:     7,
    rank:       'Explorer',
    initials:   'JU',
    /* Which days this week are "active" (index 0=Mon … 6=Sun) */
    streakDays: [true, true, true, true, false, false, false],
    /* Streak history for mini-chart (last 7 days, values 0–15) */
    streakHistory: [4, 6, 5, 9, 7, 11, 7],
  };

  /* ── Level definitions ─────────────────────────────────────── */
  const LEVELS = [
    { level: 1, name: 'Aprendiz',    xpRequired: 0    },
    { level: 2, name: 'Iniciado',    xpRequired: 500  },
    { level: 3, name: 'Practicante', xpRequired: 1000 },
    { level: 4, name: 'Avanzado',    xpRequired: 1500 },
    { level: 5, name: 'Maestro',     xpRequired: 2500 },
  ];

  /* ── Persistence helpers ────────────────────────────────────── */
  function loadProgress() {
    try {
      const raw = localStorage.getItem('skillogic_progress');
      return raw ? JSON.parse(raw) : {};
    } catch { return {}; }
  }

  function saveProgress(progress) {
    try {
      localStorage.setItem('skillogic_progress', JSON.stringify(progress));
    } catch { /* quota exceeded – silent */ }
  }

  function loadAuthState() {
    try {
      const raw = localStorage.getItem('skillogic_auth');
      if (!raw) return null;
      const { user, ts } = JSON.parse(raw);
      /* Sessions expire after 24 h */
      if (Date.now() - ts > 86_400_000) return null;
      return user;
    } catch { return null; }
  }

  function persistAuth(user) {
    try {
      localStorage.setItem('skillogic_auth', JSON.stringify({ user, ts: Date.now() }));
    } catch { /* silent */ }
  }

  function clearAuth() {
    try { localStorage.removeItem('skillogic_auth'); } catch { /* silent */ }
  }

  /* ── Public API ─────────────────────────────────────────────── */
  return {
    /* --- Getters --- */
    get: () => ({ ..._state }),

    getUser: () => _state.currentUser
      ? { ..._state.currentUser }
      : null,

    getLevelInfo: (xp = 0) => {
      for (let i = LEVELS.length - 1; i >= 0; i--) {
        if (xp >= LEVELS[i].xpRequired) return LEVELS[i];
      }
      return LEVELS[0];
    },

    getXpPercent: () => {
      if (!_state.currentUser) return 0;
      const { xp, xpToNext } = _state.currentUser;
      return Math.min(Math.round((xp / xpToNext) * 100), 100);
    },

    /* Progress for a lesson */
    getLessonProgress: (slug) => _state.userProgress[slug] || { completedExercises: [], xpEarned: 0 },

    isExerciseDone: (exerciseId) => {
      for (const prog of Object.values(_state.userProgress)) {
        if (prog.completedExercises?.includes(exerciseId)) return true;
      }
      return false;
    },

    /* --- Auth setters --- */
    login(userData) {
      const user = { ...MOCK_USER, ...userData };
      _state.currentUser = user;
      _state.isAuthenticated = true;
      _state.userProgress = loadProgress();
      persistAuth(user);
    },

    loginMock() {
      /* Login with mock data for development */
      this.login(MOCK_USER);
    },

    logout() {
      _state.currentUser = null;
      _state.isAuthenticated = false;
      clearAuth();
    },

    /* Try to restore session on app start */
    restoreSession() {
      const savedUser = loadAuthState();
      if (savedUser) {
        _state.currentUser = savedUser;
        _state.isAuthenticated = true;
        _state.userProgress = loadProgress();
        return true;
      }
      return false;
    },

    /* --- Navigation setters --- */
    setRoute(route) {
      _state.currentRoute = route;
    },

    setCurrentLesson(lesson) {
      _state.currentLesson = lesson;
    },

    setCurrentExercise(exercise) {
      _state.currentExercise = exercise;
    },

    /* --- Runtime setters --- */
    setPythonReady(val) { _state.pythonReady = val; },
    setMonacoReady(val) { _state.monacoReady = val; },

    /* --- Progress mutation --- */
    markExerciseComplete(lessonSlug, exerciseId, xpEarned) {
      const prog = _state.userProgress[lessonSlug] || { completedExercises: [], xpEarned: 0 };

      /* Idempotent: don't award XP twice */
      if (prog.completedExercises.includes(exerciseId)) return false;

      prog.completedExercises.push(exerciseId);
      prog.xpEarned += xpEarned;
      _state.userProgress[lessonSlug] = prog;

      /* Update user XP */
      if (_state.currentUser) {
        _state.currentUser.xp += xpEarned;
        persistAuth(_state.currentUser);
      }

      saveProgress(_state.userProgress);
      return true; // newly awarded
    },
  };
})();
