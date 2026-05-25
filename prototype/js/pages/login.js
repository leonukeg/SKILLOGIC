/* ================================================================
   SKILLOGIC — Login Page
   Renders the login form into the #app element.
   ================================================================ */

'use strict';

const LoginPage = {
  render() {
    return `
      <div class="auth-layout fade-in">
        <div class="auth-card">
          <!-- Logo -->
          <div class="auth-logo">
            <div class="auth-logo-mark">⚡</div>
            <span class="auth-logo-name">SKILLOGIC</span>
          </div>

          <h1 class="auth-title">Bienvenido de vuelta</h1>
          <p class="auth-subtitle">Continúa aprendiendo Python donde lo dejaste</p>

          <!-- Form -->
          <form id="login-form" novalidate>
            <div class="form-group">
              <label class="form-label" for="login-email">Correo electrónico</label>
              <input
                id="login-email"
                type="email"
                class="form-input"
                placeholder="tu@email.com"
                autocomplete="email"
                required
              />
            </div>

            <div class="form-group">
              <label class="form-label" for="login-password">Contraseña</label>
              <input
                id="login-password"
                type="password"
                class="form-input"
                placeholder="••••••••"
                autocomplete="current-password"
                required
              />
            </div>

            <div id="login-error" style="display:none; color:var(--error); font-size:var(--text-sm); margin-bottom:var(--space-3); padding: var(--space-2) var(--space-3); background:var(--error-light); border-radius:var(--radius-md);"></div>

            <button type="submit" class="form-submit" id="login-submit">
              Iniciar sesión
            </button>
          </form>

          <div class="auth-divider">o</div>

          <!-- Quick demo access -->
          <button
            id="login-demo"
            class="btn btn-secondary w-full"
            style="height:44px;"
          >
            🚀 Entrar con cuenta demo
          </button>

          <div class="auth-footer">
            ¿No tienes cuenta?
            <span class="auth-link" id="go-register">Regístrate gratis</span>
          </div>
        </div>
      </div>
    `;
  },

  bindEvents() {
    const form     = document.getElementById('login-form');
    const errorBox = document.getElementById('login-error');
    const submitBtn= document.getElementById('login-submit');

    /* Real form submit */
    form?.addEventListener('submit', (e) => {
      e.preventDefault();
      const email    = document.getElementById('login-email').value.trim();
      const password = document.getElementById('login-password').value;

      if (!email || !password) {
        LoginPage._showError(errorBox, 'Por favor, completa todos los campos.');
        return;
      }

      /* MVP: simulate login success */
      submitBtn.textContent = 'Iniciando sesión...';
      submitBtn.disabled = true;

      setTimeout(() => {
        AppState.loginMock();
        Router.navigate('/dashboard');
      }, 800);
    });

    /* Demo access */
    document.getElementById('login-demo')?.addEventListener('click', () => {
      AppState.loginMock();
      Router.navigate('/dashboard');
    });

    /* Go to register */
    document.getElementById('go-register')?.addEventListener('click', () => {
      Router.navigate('/register');
    });
  },

  _showError(el, msg) {
    el.textContent = msg;
    el.style.display = 'block';
  },
};
