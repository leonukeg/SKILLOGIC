/* ================================================================
   SKILLOGIC — App Orchestrator
   Responsibilities:
   1. Hash-based router
   2. Sidebar + topbar rendering
   3. Pyodide (Python in browser) initialization
   4. Toast notification system
   5. Global utilities
   ================================================================ */

'use strict';

/* ── Utility: escape HTML to prevent XSS ─────────────────────── */
function escapeHtml(str) {
  if (typeof str !== 'string') str = String(str ?? '');
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/* ================================================================
   PythonRunner — Wraps Pyodide execution
   Interface: PythonRunner.run(code) → Promise<{ success, output, errorType }>
   This wrapper isolates Pyodide so it can be swapped without touching page code.
   ================================================================ */
const PythonRunner = (() => {
  let _pyodide    = null;
  let _loading    = false;
  let _loadPromise= null;

  async function _initPyodide() {
    if (_pyodide) return _pyodide;
    if (_loading) return _loadPromise;

    _loading     = true;
    _loadPromise = loadPyodide({
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/',
    }).then(py => {
      _pyodide = py;
      _loading = false;
      AppState.setPythonReady(true);
      console.info('[SKILLOGIC] Pyodide ready ✓');
      return py;
    });

    return _loadPromise;
  }

  return {
    /* Start loading in background (call on app init) */
    preload() {
      _initPyodide().catch(err => {
        console.warn('[SKILLOGIC] Pyodide preload failed:', err);
      });
    },

    async run(code) {
      /* Sanitize: remove dangerous system-level imports for sandboxing */
      const forbidden = /\b(subprocess|os\.system|eval|exec|__import__)\s*\(/;
      if (forbidden.test(code)) {
        return {
          success:   false,
          output:    '',
          errorType: 'SecurityError',
        };
      }

      let py;
      try {
        py = await _initPyodide();
      } catch(err) {
        return {
          success:   false,
          output:    '',
          errorType: 'RuntimeError',
        };
      }

      /* Redirect stdout/stderr */
      const setupCode = `
import sys
from io import StringIO
_skillogic_stdout = StringIO()
sys.stdout = _skillogic_stdout
sys.stderr = _skillogic_stdout
`;

      const cleanupCode = `
import sys
_output = _skillogic_stdout.getvalue()
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
_output
`;

      try {
        py.runPython(setupCode);
        py.runPython(code);
        const output = py.runPython(cleanupCode);
        return { success: true, output: String(output ?? '') };
      } catch(err) {
        /* Extract clean output that printed before the error */
        let partialOutput = '';
        try {
          partialOutput = py.runPython(`
import sys
_o = _skillogic_stdout.getvalue()
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
_o
`);
        } catch { /* ignore */ }

        /* Identify error type for pedagogical feedback */
        const errMsg  = String(err.message || err);
        const errType = PythonRunner._extractErrorType(errMsg);

        return {
          success:   false,
          output:    String(partialOutput ?? ''),
          errorType: errType,
          rawError:  errMsg,
        };
      }
    },

    _extractErrorType(errMsg) {
      const types = [
        'IndexError', 'ZeroDivisionError', 'AttributeError', 'NameError',
        'TypeError', 'SyntaxError', 'IndentationError', 'ValueError',
        'KeyError', 'RecursionError',
      ];
      for (const t of types) {
        if (errMsg.includes(t)) return t;
      }
      return 'default';
    },
  };
})();

/* ================================================================
   Toast — notification system
   ================================================================ */
const Toast = {
  show(message, type = 'info', durationMs = 3500) {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const icons = { success: '✅', error: '❌', warning: '⚠️', info: 'ℹ️' };
    const toast  = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `
      <span style="font-size:16px;">${icons[type] || 'ℹ️'}</span>
      <span>${escapeHtml(message)}</span>
    `;

    container.appendChild(toast);

    /* Auto-remove */
    setTimeout(() => {
      toast.style.animation = 'fadeIn var(--ease-base) reverse forwards';
      setTimeout(() => toast.remove(), 250);
    }, durationMs);
  },
};

/* ================================================================
   Sidebar & Topbar renderers
   ================================================================ */
const Shell = {
  renderSidebar(activeRoute) {
    const user    = AppState.getUser();
    const xpPct   = AppState.getXpPercent();
    const weekDays= ['L','M','M','J','V','S','D'];
    const days    = user?.streakDays || Array(7).fill(false);

    const navItems = [
      { icon: '🏠', label: 'Inicio',              route: '/dashboard' },
      { icon: '🗺️', label: 'Ruta de Aprendizaje', route: '/dashboard' },
      { icon: '📖', label: 'Lecciones',            route: '/dashboard' },
      { icon: '📁', label: 'Proyectos',             route: '/dashboard' },
      { icon: '🎯', label: 'Desafíos',             route: '/dashboard' },
      { icon: '⌨️', label: 'Code Lab',             route: '/dashboard' },
      { icon: '👥', label: 'Comunidad',            route: '/dashboard' },
      { icon: '📚', label: 'Recursos',             route: '/dashboard' },
    ];

    const navHtml = navItems.map(item => {
      const isActive = activeRoute === item.route && item.label === 'Inicio';
      return `
        <div class="sidebar-nav-item ${isActive ? 'active' : ''}" data-route="${item.route}" role="button" tabindex="0">
          <span class="nav-icon">${item.icon}</span>
          ${item.label}
        </div>
      `;
    }).join('');

    const calendarHtml = weekDays.map((d, i) => `
      <div>
        <div class="streak-day-label">${d}</div>
        <div class="streak-day-dot ${days[i] ? 'active' : 'inactive'}"></div>
      </div>
    `).join('');

    return `
      <div class="sidebar-logo">
        <div class="sidebar-logo-mark">⚡</div>
        <span class="sidebar-logo-text">SKILLOGIC</span>
      </div>

      <nav class="sidebar-nav">
        ${navHtml}
      </nav>

      <!-- Progress -->
      <div class="progress-section">
        <div class="sidebar-section-label">Tu Progreso</div>
        <div class="progress-level-row">
          <span class="level-badge">${user?.level ?? 1}</span>
          <span class="xp-value">${user?.xp ?? 0} / ${user?.xpToNext ?? 500} XP</span>
        </div>
        <div class="xp-bar-track">
          <div class="xp-bar-fill" style="width:${xpPct}%;"></div>
        </div>
        <div class="rank-row">
          <span class="rank-icon">🏆</span>
          <span class="rank-label">Rango</span>
          <span class="rank-name" style="margin-left:auto;">${user?.rank ?? 'Aprendiz'}</span>
        </div>
      </div>

      <!-- Streak -->
      <div class="streak-section">
        <div class="sidebar-section-label">Racha Actual</div>
        <div class="streak-header">
          <span class="streak-fire">🔥</span>
          <span class="streak-days">${user?.streak ?? 0}</span>
          <span class="streak-days-label">días</span>
        </div>
        <div class="streak-calendar">${calendarHtml}</div>
      </div>

      <!-- Objective -->
      <div class="objective-widget">
        <div class="objective-label">Próximo objetivo</div>
        <div class="objective-value">Completa 3 ejercicios</div>
        <div class="objective-progress">1/3</div>
        <div class="module-bar-track">
          <div class="module-bar-fill" style="width:33%;"></div>
        </div>
      </div>

      <!-- CTA -->
      <div class="sidebar-cta">
        <div class="sidebar-cta-text">¿Necesitas ayuda?</div>
        <div class="sidebar-cta-sub">Únete a nuestra comunidad</div>
        <span class="sidebar-cta-btn">Ir a la comunidad →</span>
      </div>
    `;
  },

  renderTopbar() {
    const user = AppState.getUser();
    const initials = user?.initials || (user?.name?.slice(0, 2).toUpperCase()) || '??';

    return `
      <div class="topbar-search">
        <svg class="topbar-search-icon" width="14" height="14" viewBox="0 0 16 16" fill="currentColor">
          <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
        </svg>
        <input
          id="topbar-search"
          type="text"
          class="topbar-search-input"
          placeholder="Buscar lecciones, temas o desafíos..."
          aria-label="Buscar"
        />
        <kbd class="topbar-search-kbd">⌘K</kbd>
      </div>

      <div class="topbar-spacer"></div>

      <div class="topbar-streak-badge" title="Tu racha actual">
        🔥 <span>${user?.streak ?? 0} días</span>
      </div>

      <button class="topbar-icon-btn" aria-label="Notificaciones" title="Notificaciones">
        <svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor">
          <path d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2zM8 1.918l-.797.161A4.002 4.002 0 0 0 4 6c0 .628-.134 2.197-.459 3.742-.16.767-.376 1.566-.663 2.258h10.244c-.287-.692-.502-1.49-.663-2.258C12.134 8.197 12 6.628 12 6a4.002 4.002 0 0 0-3.203-3.92L8 1.917zM14.22 12c.223.447.481.801.78 1H1c.299-.199.557-.553.78-1C2.68 10.2 3 6.88 3 6c0-2.42 1.72-4.44 4.005-4.901a1 1 0 1 1 1.99 0A5.002 5.002 0 0 1 13 6c0 .88.32 4.2 1.22 6z"/>
        </svg>
        <div class="notification-dot"></div>
      </button>

      <div class="topbar-avatar" id="topbar-user-menu" title="${user?.name ?? 'Usuario'}">
        ${initials}
      </div>
    `;
  },

  bindSidebarEvents() {
    document.querySelectorAll('.sidebar-nav-item[data-route]').forEach(item => {
      item.addEventListener('click', () => {
        Router.navigate(item.dataset.route);
      });
    });
  },

  bindTopbarEvents() {
    document.getElementById('topbar-user-menu')?.addEventListener('click', () => {
      /* MVP: simple logout option */
      if (confirm('¿Cerrar sesión?')) {
        AppState.logout();
        Router.navigate('/login');
      }
    });
  },
};

/* ================================================================
   Router — Hash-based SPA router
   ================================================================ */
const Router = {
  _routes: {},

  register(path, handlers) {
    this._routes[path] = handlers;
  },

  navigate(path) {
    window.location.hash = path;
  },

  _resolve(hash) {
    const path = hash.replace(/^#/, '') || '/';

    /* Auth guard */
    const protectedRoutes = ['/dashboard', '/lessons', '/lesson'];
    const isProtected     = protectedRoutes.some(r => path.startsWith(r));
    const isAuth          = AppState.get().isAuthenticated;

    if (isProtected && !isAuth) {
      return Router.navigate('/login');
    }

    if ((path === '/login' || path === '/register') && isAuth) {
      return Router.navigate('/dashboard');
    }

    /* Parse lesson slug: /lesson/:slug */
    if (path.startsWith('/lesson/')) {
      const slug = path.replace('/lesson/', '');
      Router._renderPage('lesson', slug);
      return;
    }

    /* Default routes */
    const routeMap = {
      '/':          () => isAuth ? Router.navigate('/dashboard') : Router.navigate('/login'),
      '/login':     () => Router._renderPage('login'),
      '/register':  () => Router._renderPage('register'),
      '/dashboard': () => Router._renderPage('dashboard'),
    };

    const handler = routeMap[path];
    if (handler) {
      handler();
    } else {
      /* 404 → dashboard or login */
      Router.navigate(isAuth ? '/dashboard' : '/login');
    }
  },

  _renderPage(page, param) {
    const app       = document.getElementById('app');
    const isAuthPage= page === 'login' || page === 'register';

    AppState.setRoute(page === 'lesson' ? `/lesson/${param}` : `/${page}`);

    if (isAuthPage) {
      /* Auth layout: no sidebar */
      app.innerHTML = `
        <div class="sk-app" style="width:100%;">
          <div id="page-root"></div>
        </div>
      `;

      const pageRoot = document.getElementById('page-root');
      if (page === 'login') {
        pageRoot.innerHTML = LoginPage.render();
        LoginPage.bindEvents();
      } else {
        pageRoot.innerHTML = RegisterPage.render();
        RegisterPage.bindEvents();
      }
      return;
    }

    /* App layout: with sidebar + topbar */
    app.innerHTML = `
      <div class="app-layout">
        <!-- Sidebar -->
        <aside class="sidebar" id="sidebar-root">
          ${Shell.renderSidebar(`/${page}`)}
        </aside>

        <!-- Main area -->
        <div class="main-area" id="main-area">
          <!-- Topbar -->
          <header class="topbar" id="topbar-root">
            ${Shell.renderTopbar()}
          </header>

          <!-- Page content -->
          <main class="page-content" id="page-root"></main>
        </div>
      </div>

      <!-- Toast container stays outside layout -->
      <div id="toast-container" class="toast-container"></div>
    `;

    Shell.bindSidebarEvents();
    Shell.bindTopbarEvents();

    const pageRoot = document.getElementById('page-root');

    if (page === 'dashboard') {
      pageRoot.innerHTML = DashboardPage.render();
      DashboardPage.afterRender();

    } else if (page === 'lesson') {
      pageRoot.innerHTML = LessonPage.render(param);
      LessonPage.afterRender(param);
    }
  },
};

/* ================================================================
   App Bootstrap
   ================================================================ */
(function boot() {
  /* 1. Restore session if possible */
  AppState.restoreSession();

  /* 2. Start preloading Python in the background */
  PythonRunner.preload();

  /* 3. Listen to hash changes (navigation) */
  window.addEventListener('hashchange', () => {
    Router._resolve(window.location.hash);
  });

  /* 4. Resolve initial route */
  const initialHash = window.location.hash || '#/';
  Router._resolve(initialHash);

  /* 5. Keyboard shortcut: ⌘K / Ctrl+K → focus search */
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      document.getElementById('topbar-search')?.focus();
    }
  });

  console.info('[SKILLOGIC] App booted ✓');
})();
