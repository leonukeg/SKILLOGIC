/* ================================================================
   SKILLOGIC — Dashboard Page
   Main screen: hero + learning path + lesson preview + right panel
   ================================================================ */

'use strict';

const DashboardPage = {

  render() {
    const user    = AppState.getUser();
    const data    = SKILLOGIC_DATA;
    const lessons = data.lessons;
    const currentLesson = lessons.find(l => !l.completed) || lessons[lessons.length - 1];

    return `
      <div class="dashboard-layout fade-in">
        <!-- ── Main Content ── -->
        <div class="dashboard-main">
          ${DashboardPage._renderHero(user)}
          ${DashboardPage._renderLearningPath(data.modules)}
          ${DashboardPage._renderCurrentLesson(currentLesson)}
          ${DashboardPage._renderProjectCards(lessons)}
        </div>

        <!-- ── Right Panel ── -->
        <aside class="dashboard-right">
          ${DashboardPage._renderStreakWidget(user)}
          ${DashboardPage._renderPlanToday(data.todayPlan)}
          ${DashboardPage._renderDailyChallenge()}
          ${DashboardPage._renderCommunityFeed(data.communityFeed)}
        </aside>
      </div>
    `;
  },

  /* ── Hero ───────────────────────────────────────────────────── */
  _renderHero(user) {
    const name = user?.name || 'Estudiante';
    return `
      <div class="hero-card">
        <div class="hero-content">
          <h1 class="hero-title">
            Aprende Python.<br>
            <span class="hero-title-accent">Construye el futuro. 🚀</span>
          </h1>
          <p class="hero-subtitle">
            Un camino práctico, moderno y efectivo para llevar tus habilidades de Python al siguiente nivel.
          </p>
          <div class="hero-actions">
            <button class="btn btn-primary btn-lg" id="hero-continue-btn">
              ▶ Continuar aprendiendo
            </button>
            <button class="btn btn-secondary btn-lg" id="hero-route-btn">
              Ver mi ruta
            </button>
          </div>
        </div>
        <div class="hero-visual">🐍</div>
      </div>
    `;
  },

  /* ── Learning path ──────────────────────────────────────────── */
  _renderLearningPath(modules) {
    const cards = modules.map((mod, i) => {
      const statusClass = mod.status === 'completed' ? 'completed'
                        : mod.status === 'active'    ? 'active'
                        : '';
      return `
        <div class="module-card ${statusClass}" data-module="${mod.id}" role="button" tabindex="0">
          <span class="module-icon">${mod.emoji}</span>
          <div class="module-name">${i + 1}. ${mod.title}</div>
          <div class="module-progress-pct">${mod.progress}%</div>
          <div class="module-bar-track">
            <div class="module-bar-fill" style="width:${mod.progress}%"></div>
          </div>
        </div>
        ${i < modules.length - 1 ? '<div class="module-connector">→</div>' : ''}
      `;
    }).join('');

    return `
      <div>
        <div class="section-header">
          <h2 class="section-title">Tu ruta de aprendizaje</h2>
          <span class="section-link" id="view-full-route">Ver ruta completa →</span>
        </div>
        <div class="learning-path">${cards}</div>
      </div>
    `;
  },

  /* ── Current lesson with code preview ──────────────────────── */
  _renderCurrentLesson(lesson) {
    if (!lesson) return '';
    const exercise = lesson.exercises[0];

    return `
      <div class="lesson-card-full">
        <div class="lesson-card-header">
          <div>
            <div class="lesson-card-label">Lección actual</div>
            <div class="lesson-card-title">${lesson.title}</div>
          </div>
          <div class="flex gap-2 items-center">
            <span class="lesson-xp-badge">⭐ ${exercise.xp} XP</span>
            <button class="btn btn-primary btn-sm" id="open-lesson-btn" data-slug="${lesson.slug}">
              Abrir lección
            </button>
          </div>
        </div>

        <!-- Tabs -->
        <div class="lesson-tabs">
          <div class="lesson-tab active" data-tab="instructions">📖 Instrucciones</div>
          <div class="lesson-tab" data-tab="hint">💡 Pista</div>
          <div class="lesson-tab" data-tab="discussion">💬 Discusión</div>
        </div>

        <!-- 3-panel editor preview -->
        <div class="lesson-editor">
          <!-- Instructions panel -->
          <div class="lesson-instructions">
            <h4>${exercise.title}</h4>
            <p>${exercise.description}</p>
            <div class="code-example">${lesson.codeExample}</div>
          </div>

          <!-- Code editor (Monaco, read-only preview) -->
          <div class="monaco-wrapper">
            <div class="monaco-lang-bar">
              <div class="monaco-lang-badge">
                <span style="color:var(--brand);">●</span> Python 3
              </div>
              <button class="btn btn-ghost btn-sm" id="reset-dashboard-code">⟳ Reiniciar</button>
            </div>
            <div id="dashboard-monaco" class="monaco-container" style="height:280px;"></div>
          </div>

          <!-- Output panel -->
          <div class="output-panel">
            <div class="output-panel-title">Salida</div>
            <div id="dashboard-output-area">
              <div class="output-result neutral" style="font-style:italic; color:var(--text-muted);">
                Ejecuta el código para ver la salida
              </div>
            </div>
          </div>
        </div>

        <!-- Actions bar -->
        <div class="lesson-card-actions">
          <button class="btn btn-ghost btn-sm" id="dashboard-hint-btn">
            💡 Ver pista
          </button>
          <div class="flex gap-2">
            <button class="btn btn-secondary btn-sm" id="dashboard-reset-btn">⟳ Reiniciar</button>
            <button class="btn btn-primary" id="dashboard-run-btn">
              ▶ Ejecutar
            </button>
          </div>
        </div>
      </div>
    `;
  },

  /* ── Projects grid ──────────────────────────────────────────── */
  _renderProjectCards(lessons) {
    const projects = [
      { icon: '🔐', title: 'Generador de Contraseñas', level: 'intermediate', progress: 75 },
      { icon: '🌐', title: 'Web Scraper',               level: 'basic',        progress: 0  },
      { icon: '📋', title: 'Lista de Tareas',           level: 'intermediate', progress: 25 },
      { icon: '📊', title: 'Análisis de Datos',         level: 'advanced',     progress: 0  },
    ];

    const levelLabels = { basic: 'Básico', intermediate: 'Intermedio', advanced: 'Avanzado' };

    const cards = projects.map(p => `
      <div class="lesson-mini-card" role="button" tabindex="0">
        <div class="lesson-mini-icon">${p.icon}</div>
        <div class="lesson-mini-info">
          <div class="lesson-mini-title">${p.title}</div>
          <div class="lesson-mini-sub" style="margin-top:4px;">
            <span class="difficulty-badge ${p.level}">${levelLabels[p.level]}</span>
          </div>
          ${p.progress > 0 ? `
            <div class="module-bar-track" style="margin-top:6px;">
              <div class="module-bar-fill" style="width:${p.progress}%;"></div>
            </div>
          ` : ''}
        </div>
      </div>
    `).join('');

    return `
      <div>
        <div class="section-header">
          <h2 class="section-title">Proyectos para ti</h2>
          <span class="section-link">Ver todos →</span>
        </div>
        <div class="lesson-grid">${cards}</div>
      </div>
    `;
  },

  /* ── Right panel: Streak widget ─────────────────────────────── */
  _renderStreakWidget(user) {
    const days     = user?.streak || 0;
    const history  = user?.streakHistory || [0,0,0,0,0,0,0];
    const weekDays = user?.streakDays   || Array(7).fill(false);
    const dayNames = ['L','M','M','J','V','S','D'];

    /* Build SVG mini-chart */
    const maxVal = Math.max(...history, 1);
    const w = 240, h = 56, padding = 8;
    const stepX = (w - padding * 2) / (history.length - 1);
    const points = history.map((v, i) => {
      const x = padding + i * stepX;
      const y = h - padding - ((v / maxVal) * (h - padding * 2));
      return `${x},${y}`;
    }).join(' ');

    const chartSvg = `
      <svg class="mini-chart" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="chartGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="var(--brand)" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="var(--brand)" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <!-- Fill area -->
        <polygon
          points="${points} ${padding + (history.length-1)*stepX},${h} ${padding},${h}"
          fill="url(#chartGrad)"
        />
        <!-- Line -->
        <polyline
          points="${points}"
          fill="none"
          stroke="var(--brand)"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
        <!-- Last point dot -->
        ${(() => {
          const lastX = padding + (history.length - 1) * stepX;
          const lastY = h - padding - ((history[history.length-1] / maxVal) * (h - padding * 2));
          return `<circle cx="${lastX}" cy="${lastY}" r="4" fill="var(--brand)" stroke="var(--bg-secondary)" stroke-width="2"/>`;
        })()}
      </svg>
    `;

    const calendarDots = dayNames.map((d, i) => {
      const cls = weekDays[i]
        ? (i === new Date().getDay() === 0 ? 6 : new Date().getDay() - 1) ? 'active' : 'active'
        : 'inactive';
      return `
        <div>
          <div class="streak-day-label">${d}</div>
          <div class="streak-day-dot ${weekDays[i] ? 'active' : 'inactive'}"></div>
        </div>
      `;
    }).join('');

    return `
      <div class="right-panel-section">
        <div class="right-section-title flex items-center gap-2">
          Racha actual 🔥
        </div>
        <div class="streak-widget-large">
          <div class="streak-widget-days">${days} días</div>
          <div class="streak-widget-label">¡Sigue así! 👋</div>
        </div>
        ${chartSvg}
        <div class="streak-calendar">${calendarDots}</div>
      </div>
    `;
  },

  /* ── Right panel: Plan today ─────────────────────────────────── */
  _renderPlanToday(plan) {
    const items = plan.map(item => `
      <div class="plan-item" id="plan-${item.id}">
        <div class="plan-check ${item.done ? 'done' : ''}"></div>
        <div class="plan-info">
          <div class="plan-name" style="${item.done ? 'text-decoration:line-through; color:var(--text-muted);' : ''}">${item.title}</div>
          <div class="plan-sub">${item.sub}</div>
        </div>
      </div>
    `).join('');

    return `
      <div class="right-panel-section">
        <div class="flex items-center justify-between" style="margin-bottom:var(--space-3);">
          <div class="right-section-title">Plan de hoy</div>
          <span class="section-link" style="font-size:var(--text-xs);">Ver todo</span>
        </div>
        ${items}
        <button class="btn btn-primary w-full btn-sm" style="margin-top:var(--space-3);">
          Continuar plan
        </button>
      </div>
    `;
  },

  /* ── Right panel: Daily challenge ───────────────────────────── */
  _renderDailyChallenge() {
    return `
      <div class="right-panel-section">
        <div class="flex items-center justify-between" style="margin-bottom:var(--space-3);">
          <div class="right-section-title">Desafío diario</div>
          <span class="new-badge">Nuevo</span>
        </div>
        <div class="challenge-card">
          <div class="challenge-header">
            <div class="challenge-title">Suma de números pares</div>
          </div>
          <div class="challenge-difficulty">
            Dificultad: <span>Fácil</span>
          </div>
          <div class="challenge-desc">
            Crea una función que reciba un número n y devuelva la suma de todos los números pares hasta n.
          </div>
          <button class="btn btn-primary w-full btn-sm" id="challenge-resolve-btn">
            ▶ Resolver desafío
          </button>
        </div>
        <span class="section-link" style="font-size:var(--text-xs); display:block; margin-top:var(--space-3);">
          Ver todos los desafíos →
        </span>
      </div>
    `;
  },

  /* ── Right panel: Community feed ─────────────────────────────── */
  _renderCommunityFeed(feed) {
    const colors = ['#7C3AED','#2EA043','#F97316','#388BFD','#D29922'];
    const items = feed.map((item, i) => `
      <div class="community-item">
        <div class="community-avatar" style="background:${colors[i % colors.length]};">
          ${item.initials}
        </div>
        <div class="community-text">
          <div class="community-msg">${item.msg}</div>
          <div class="community-time">${item.time}</div>
        </div>
      </div>
    `).join('');

    return `
      <div class="right-panel-section">
        <div class="right-section-title">Comunidad activa</div>
        ${items}
        <button class="btn btn-ghost w-full btn-sm" style="margin-top:var(--space-2);">
          Ir a la comunidad →
        </button>
      </div>
    `;
  },

  /* ── After render: initialize Monaco in dashboard preview ───── */
  afterRender() {
    const lesson   = SKILLOGIC_DATA.lessons.find(l => !l.completed) || SKILLOGIC_DATA.lessons[0];
    const exercise = lesson.exercises[0];

    /* Init Monaco in dashboard preview */
    require.config({ paths: { vs: 'https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs' } });
    require(['vs/editor/editor.main'], () => {
      AppState.setMonacoReady(true);

      window._dashboardEditor = monaco.editor.create(
        document.getElementById('dashboard-monaco'),
        {
          value:               exercise.starterCode,
          language:            'python',
          theme:               'vs-dark',
          fontSize:            13,
          fontFamily:          "'JetBrains Mono', monospace",
          minimap:             { enabled: false },
          scrollBeyondLastLine: false,
          lineNumbers:         'on',
          automaticLayout:     true,
          padding:             { top: 12, bottom: 12 },
          renderLineHighlight: 'none',
          overviewRulerLanes:  0,
          folding:             false,
          lineDecorationsWidth: 4,
        }
      );
    });

    DashboardPage._bindEvents(lesson, exercise);
  },

  _bindEvents(lesson, exercise) {
    /* Continue btn → open lesson */
    document.getElementById('hero-continue-btn')?.addEventListener('click', () => {
      Router.navigate(`/lesson/${lesson.slug}`);
    });

    document.getElementById('hero-route-btn')?.addEventListener('click', () => {
      document.querySelector('.learning-path')?.scrollIntoView({ behavior: 'smooth' });
    });

    document.getElementById('open-lesson-btn')?.addEventListener('click', (e) => {
      Router.navigate(`/lesson/${e.target.dataset.slug}`);
    });

    /* Module cards */
    document.querySelectorAll('.module-card').forEach(card => {
      card.addEventListener('click', () => {
        const modId = parseInt(card.dataset.module);
        const targetLesson = SKILLOGIC_DATA.lessons.find(l => l.module === modId);
        if (targetLesson) Router.navigate(`/lesson/${targetLesson.slug}`);
      });
    });

    /* Run code in dashboard preview */
    document.getElementById('dashboard-run-btn')?.addEventListener('click', () => {
      DashboardPage._runDashboardCode(lesson, exercise);
    });

    document.getElementById('dashboard-reset-btn')?.addEventListener('click', () => {
      window._dashboardEditor?.setValue(exercise.starterCode);
    });

    document.getElementById('reset-dashboard-code')?.addEventListener('click', () => {
      window._dashboardEditor?.setValue(exercise.starterCode);
    });

    /* Hint */
    document.getElementById('dashboard-hint-btn')?.addEventListener('click', () => {
      Toast.show(exercise.hints[0], 'warning');
    });

    /* Lesson tabs */
    document.querySelectorAll('.lesson-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        document.querySelectorAll('.lesson-tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
      });
    });

    /* Challenge */
    document.getElementById('challenge-resolve-btn')?.addEventListener('click', () => {
      Router.navigate(`/lesson/${lesson.slug}`);
    });
  },

  /* ── Execute code in dashboard panel ────────────────────────── */
  async _runDashboardCode(lesson, exercise) {
    const runBtn    = document.getElementById('dashboard-run-btn');
    const outputArea= document.getElementById('dashboard-output-area');
    const code      = window._dashboardEditor?.getValue() || '';

    runBtn.textContent = '⏳ Ejecutando...';
    runBtn.disabled    = true;

    try {
      const result = await PythonRunner.run(code);
      outputArea.innerHTML = DashboardPage._buildOutputHtml(result, exercise);
    } catch(err) {
      outputArea.innerHTML = `<div class="output-result error">❌ Error inesperado</div>`;
    } finally {
      runBtn.textContent = '▶ Ejecutar';
      runBtn.disabled    = false;
    }
  },

  _buildOutputHtml(result, exercise) {
    let html = '';

    if (result.output) {
      html += `<div class="output-text">${escapeHtml(result.output)}</div>`;
    }

    if (!result.success) {
      const errType   = result.errorType || 'default';
      const pedMsg    = SKILLOGIC_DATA.errorFeedback[errType] || SKILLOGIC_DATA.errorFeedback.default;
      html += `<div class="output-result error">❌ ${escapeHtml(pedMsg)}</div>`;
      return html;
    }

    /* Check tests */
    let allPass = true;
    exercise.tests.forEach(test => {
      const pass = test.check(result.output);
      if (!pass) allPass = false;
      html += `<div class="output-result ${pass ? 'success' : 'error'}">
        ${pass ? '✅' : '❌'} ${test.description}
      </div>`;
    });

    if (allPass) {
      Toast.show(`¡Correcto! +${exercise.xp} XP 🎉`, 'success');
      AppState.markExerciseComplete(AppState.get().currentLesson?.slug || '', exercise.id, exercise.xp);
    }

    return html;
  },
};
