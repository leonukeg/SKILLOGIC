/* ================================================================
   SKILLOGIC — Register Page
   ================================================================ */

'use strict';

const RegisterPage = {
  render() {
    return `
      <div class="auth-layout fade-in">
        <div class="auth-card">
          <!-- Logo -->
          <div class="auth-logo">
            <div class="auth-logo-mark">⚡</div>
            <span class="auth-logo-name">SKILLOGIC</span>
          </div>

          <h1 class="auth-title">Empieza a programar</h1>
          <p class="auth-subtitle">Gratis para siempre. Sin tarjeta de crédito.</p>

          <form id="register-form" novalidate>
            <div class="form-group">
              <label class="form-label" for="reg-name">Tu nombre</label>
              <input
                id="reg-name"
                type="text"
                class="form-input"
                placeholder="Ana García"
                autocomplete="name"
                required
              />
            </div>

            <div class="form-group">
              <label class="form-label" for="reg-email">Correo electrónico</label>
              <input
                id="reg-email"
                type="email"
                class="form-input"
                placeholder="tu@email.com"
                autocomplete="email"
                required
              />
            </div>

            <div class="form-group">
              <label class="form-label" for="reg-password">Contraseña</label>
              <input
                id="reg-password"
                type="password"
                class="form-input"
                placeholder="Mínimo 8 caracteres"
                autocomplete="new-password"
                required
              />
              <div id="password-strength" style="margin-top:var(--space-1); font-size:var(--text-xs); color:var(--text-muted);"></div>
            </div>

            <div id="register-error" style="display:none; color:var(--error); font-size:var(--text-sm); margin-bottom:var(--space-3); padding: var(--space-2) var(--space-3); background:var(--error-light); border-radius:var(--radius-md);"></div>

            <!-- Terms -->
            <p style="font-size:var(--text-xs); color:var(--text-muted); margin-bottom:var(--space-4); line-height:1.5;">
              Al registrarte aceptas nuestros
              <span style="color:var(--brand);">Términos de uso</span> y
              <span style="color:var(--brand);">Política de privacidad</span>.
            </p>

            <button type="submit" class="form-submit" id="register-submit">
              Crear cuenta gratis
            </button>
          </form>

          <div class="auth-footer">
            ¿Ya tienes cuenta?
            <span class="auth-link" id="go-login">Iniciar sesión</span>
          </div>
        </div>
      </div>
    `;
  },

  bindEvents() {
    const form      = document.getElementById('register-form');
    const errorBox  = document.getElementById('register-error');
    const submitBtn = document.getElementById('register-submit');
    const pwdInput  = document.getElementById('reg-password');
    const strengthEl= document.getElementById('password-strength');

    /* Live password strength indicator */
    pwdInput?.addEventListener('input', () => {
      const val = pwdInput.value;
      const strength = RegisterPage._checkPasswordStrength(val);
      strengthEl.textContent = strength.label;
      strengthEl.style.color = strength.color;
    });

    form?.addEventListener('submit', (e) => {
      e.preventDefault();
      const name     = document.getElementById('reg-name').value.trim();
      const email    = document.getElementById('reg-email').value.trim();
      const password = pwdInput.value;

      if (!name || !email || !password) {
        RegisterPage._showError(errorBox, 'Por favor, completa todos los campos.');
        return;
      }

      if (password.length < 8) {
        RegisterPage._showError(errorBox, 'La contraseña debe tener al menos 8 caracteres.');
        return;
      }

      submitBtn.textContent = 'Creando cuenta...';
      submitBtn.disabled = true;

      /* MVP: simulate registration */
      setTimeout(() => {
        AppState.loginMock();
        Router.navigate('/dashboard');
        Toast.show('¡Bienvenido a SKILLOGIC! 🚀', 'success');
      }, 900);
    });

    document.getElementById('go-login')?.addEventListener('click', () => {
      Router.navigate('/login');
    });
  },

  _showError(el, msg) {
    el.textContent = msg;
    el.style.display = 'block';
  },

  _checkPasswordStrength(pwd) {
    if (pwd.length === 0) return { label: '', color: 'var(--text-muted)' };
    if (pwd.length < 6)   return { label: 'Demasiado corta', color: 'var(--error)' };

    let score = 0;
    if (pwd.length >= 8)                            score++;
    if (/[A-Z]/.test(pwd))                          score++;
    if (/[0-9]/.test(pwd))                          score++;
    if (/[^A-Za-z0-9]/.test(pwd))                   score++;

    if (score <= 1) return { label: 'Débil', color: 'var(--warning)' };
    if (score === 2) return { label: 'Regular', color: 'var(--warning)' };
    if (score === 3) return { label: 'Buena',   color: 'var(--success)' };
    return { label: '¡Excelente!', color: 'var(--success)' };
  },
};
