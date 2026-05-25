/* ================================================================
   SKILLOGIC — Lesson Page
   Full-screen 3-panel layout:
   Left: description + exercise selector
   Center: Monaco Editor (full height)
   Right: output + test results
   ================================================================ */

'use strict';

const LessonPage = {
  _monacoInstance: null,
  _currentExercise: null,
  _hintVisible: false,

  render(lessonSlug) {
    const lesson = SKILLOGIC_DATA.lessons.find(l => l.slug === lessonSlug);
    if (!lesson) {
      return `<div style="padding:var(--space-8); color:var(--text-muted);">Lección no encontrada.</div>`;
    }

    AppState.setCurrentLesson(lesson);
    const exercise = lesson.exercises[0];
    AppState.setCurrentExercise(exercise);
    LessonPage._currentExercise = exercise;
    LessonPage._hintVisible     = false;

    return `
      <div class="lesson-page fade-in">
        <!-- Left panel: description + exercise nav -->
        <div class="lesson-sidebar-panel">
          ${LessonPage._renderLessonHeader(lesson)}
          ${LessonPage._renderDescription(lesson)}
          ${LessonPage._renderExerciseNav(lesson)}
        </div>

        <!-- Center: Monaco editor -->
        <div class="lesson-editor-main">
          ${LessonPage._renderEditorToolbar(lesson)}
          <div id="full-monaco-container" class="full-monaco-container"></div>
          <!-- Python status bar -->
          <div class="python-status-bar" id="python-status-bar">
            <div class="python-status-dot" id="python-status-dot"></div>
            <span id="python-status-text">Cargando Python...</span>
          </div>
        </div>

        <!-- Right panel: output -->
        ${LessonPage._renderOutputPanel(exercise)}
      </div>
    `;
  },

  _renderLessonHeader(lesson) {
    return `
      <div class="lesson-sidebar-header">
        <div class="lesson-breadcrumb">
          <span style="cursor:pointer; color:var(--brand);" id="back-to-dashboard">← Dashboard</span>
          <span>/</span>
          <span>Módulo ${lesson.module}</span>
        </div>
        <div class="lesson-page-title">${lesson.title}</div>
        <div style="font-size:var(--text-xs); color:var(--text-muted); margin-top:var(--space-1);">
          ${lesson.concept}
        </div>
      </div>
    `;
  },

  _renderDescription(lesson) {
    const descHtml = lesson.description
      .replace(/\n\n/g, '</p><p>')
      .replace(/^/, '<p>')
      .replace(/$/, '</p>');

    return `
      <div class="lesson-description">
        <div style="font-size:var(--text-xs); color:var(--warning); background:var(--warning-light);
          padding:var(--space-2) var(--space-3); border-radius:var(--radius-md);
          margin-bottom:var(--space-4); font-style:italic;">
          💡 "${lesson.hook}"
        </div>
        ${descHtml}
      </div>
    `;
  },

  _renderExerciseNav(lesson) {
    const levelIcons = { basic: '🟢', intermediate: '🟡', advanced: '🔴' };
    const items = lesson.exercises.map((ex, i) => {
      const isDone = AppState.isExerciseDone(ex.id);
      return `
        <button
          class="exercise-btn ${i === 0 ? 'active' : ''}"
          id="ex-btn-${ex.id}"
          data-exercise-id="${ex.id}"
          data-lesson-slug="${lesson.slug}"
          data-index="${i}"
        >
          <div class="flex items-center gap-2">
            <span>${isDone ? '✅' : levelIcons[ex.level]}</span>
            <span class="exercise-btn-label">${ex.levelLabel}</span>
          </div>
          <span class="exercise-xp">+${ex.xp} XP</span>
        </button>
      `;
    }).join('');

    return `
      <div class="exercise-nav">
        <div class="exercise-nav-title">Ejercicios</div>
        ${items}
        <div class="hint-box" id="lesson-hint-box">
          💡 <strong>Pista:</strong> <span id="hint-text"></span>
        </div>
      </div>
    `;
  },

  _renderEditorToolbar(lesson) {
    return `
      <div class="lesson-editor-toolbar">
        <div class="editor-info">
          <div class="editor-lang">
            <span style="color:var(--brand);">●</span>
            Python 3.12
          </div>
          <span id="editor-exercise-title" style="color:var(--text-secondary);">
            ${lesson.exercises[0].title}
          </span>
        </div>
        <div class="editor-actions">
          <button class="btn btn-ghost btn-sm" id="lesson-hint-btn" title="Ver pista">
            💡 Pista
          </button>
          <button class="btn btn-secondary btn-sm" id="lesson-reset-btn" title="Reiniciar código">
            ⟳ Reiniciar
          </button>
          <button class="btn btn-primary" id="lesson-run-btn">
            ▶ Ejecutar
          </button>
        </div>
      </div>
    `;
  },

  _renderOutputPanel(exercise) {
    const testItems = exercise.tests.map(test => `
      <div class="test-item">
        <div class="test-status pending" data-test="${exercise.id}_${test.description}"></div>
        <span class="test-label">${test.description}</span>
      </div>
    `).join('');

    return `
      <div class="lesson-output-panel">
        <div class="output-panel-header">
          <div class="output-panel-header-title">Salida</div>
          <button class="btn btn-ghost btn-sm" id="clear-output-btn" style="font-size:10px;">Limpiar</button>
        </div>
        <div class="output-body" id="output-body">
          <div class="run-status idle" id="run-status">
            <span id="run-status-text"></span>
          </div>

          <div id="terminal-output-container" style="display:none;">
            <div class="output-panel-title">Stdout</div>
            <div class="terminal-output" id="terminal-output"></div>
          </div>

          <div class="tests-section" id="tests-section">
            <div class="tests-title">Tests</div>
            <div id="tests-list">${testItems}</div>
          </div>

          <div id="feedback-box" style="display:none; margin-top:var(--space-3);
            padding:var(--space-3); background:var(--error-light);
            border-radius:var(--radius-md); font-size:var(--text-sm);
            color:var(--error); line-height:1.6;">
          </div>
        </div>
      </div>
    `;
  },

  /* ── After render: init Monaco + bind events ─────────────────── */
  afterRender(lessonSlug) {
    const lesson   = SKILLOGIC_DATA.lessons.find(l => l.slug === lessonSlug);
    if (!lesson) return;

    /* Init Monaco */
    require.config({ paths: { vs: 'https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs' } });
    require(['vs/editor/editor.main'], () => {
      AppState.setMonacoReady(true);

      if (LessonPage._monacoInstance) {
        LessonPage._monacoInstance.dispose();
      }

      LessonPage._monacoInstance = monaco.editor.create(
        document.getElementById('full-monaco-container'),
        {
          value:                 lesson.exercises[0].starterCode,
          language:              'python',
          theme:                 'vs-dark',
          fontSize:              14,
          fontFamily:            "'JetBrains Mono', monospace",
          minimap:               { enabled: false },
          scrollBeyondLastLine:  false,
          lineNumbers:           'on',
          automaticLayout:       true,
          padding:               { top: 16, bottom: 16 },
          renderLineHighlight:   'all',
          wordWrap:              'on',
          folding:               false,
          bracketPairColorization: { enabled: true },
        }
      );

      /* Ctrl+Enter → run */
      LessonPage._monacoInstance.addCommand(
        monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter,
        () => LessonPage._runCode(lesson)
      );
    });

    /* Update Python status bar */
    LessonPage._updatePythonStatus();

    LessonPage._bindLessonEvents(lesson);
  },

  _updatePythonStatus() {
    const dot  = document.getElementById('python-status-dot');
    const text = document.getElementById('python-status-text');
    const bar  = document.getElementById('python-status-bar');

    if (AppState.get().pythonReady) {
      dot?.classList.add('ready');
      if (text) text.textContent = 'Python listo ✓';
      if (bar)  bar.style.background = 'var(--success-light)';
    } else {
      if (text) text.textContent = 'Cargando Python... (primera vez puede tardar unos segundos)';
    }

    /* Poll until ready */
    const interval = setInterval(() => {
      if (AppState.get().pythonReady) {
        dot?.classList.add('ready');
        if (text) text.textContent = 'Python listo ✓';
        if (bar)  bar.style.background = 'var(--success-light)';
        clearInterval(interval);
      }
    }, 500);
  },

  _bindLessonEvents(lesson) {
    /* Back to dashboard */
    document.getElementById('back-to-dashboard')?.addEventListener('click', () => {
      Router.navigate('/dashboard');
    });

    /* Exercise selector */
    document.querySelectorAll('.exercise-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const exId    = btn.dataset.exerciseId;
        const exIndex = parseInt(btn.dataset.index);
        const ex      = lesson.exercises[exIndex];
        if (!ex) return;

        LessonPage._switchExercise(lesson, ex);
      });
    });

    /* Run button */
    document.getElementById('lesson-run-btn')?.addEventListener('click', () => {
      LessonPage._runCode(lesson);
    });

    /* Reset */
    document.getElementById('lesson-reset-btn')?.addEventListener('click', () => {
      const ex = LessonPage._currentExercise;
      if (ex) LessonPage._monacoInstance?.setValue(ex.starterCode);
    });

    /* Hint */
    document.getElementById('lesson-hint-btn')?.addEventListener('click', () => {
      LessonPage._toggleHint();
    });

    /* Clear output */
    document.getElementById('clear-output-btn')?.addEventListener('click', () => {
      LessonPage._clearOutput();
    });
  },

  _switchExercise(lesson, exercise) {
    LessonPage._currentExercise = exercise;
    AppState.setCurrentExercise(exercise);
    LessonPage._hintVisible = false;

    /* Update editor */
    LessonPage._monacoInstance?.setValue(exercise.starterCode);

    /* Update UI */
    document.querySelectorAll('.exercise-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.exerciseId === exercise.id);
    });

    const titleEl = document.getElementById('editor-exercise-title');
    if (titleEl) titleEl.textContent = exercise.title;

    /* Rebuild test list */
    const testsList = document.getElementById('tests-list');
    if (testsList) {
      testsList.innerHTML = exercise.tests.map(test => `
        <div class="test-item">
          <div class="test-status pending" data-test="${exercise.id}_${test.description}"></div>
          <span class="test-label">${test.description}</span>
        </div>
      `).join('');
    }

    /* Hide hint */
    const hintBox = document.getElementById('lesson-hint-box');
    if (hintBox) hintBox.classList.remove('visible');

    LessonPage._clearOutput();
  },

  _toggleHint() {
    LessonPage._hintVisible = !LessonPage._hintVisible;
    const hintBox  = document.getElementById('lesson-hint-box');
    const hintText = document.getElementById('hint-text');
    const ex       = LessonPage._currentExercise;

    if (hintBox && hintText && ex) {
      hintText.textContent = ex.hints[0] || 'Sin pistas disponibles para este ejercicio.';
      hintBox.classList.toggle('visible', LessonPage._hintVisible);
    }
  },

  _clearOutput() {
    const termContainer = document.getElementById('terminal-output-container');
    const termEl        = document.getElementById('terminal-output');
    const runStatus     = document.getElementById('run-status');
    const feedbackBox   = document.getElementById('feedback-box');

    if (termContainer) termContainer.style.display = 'none';
    if (termEl) termEl.textContent = '';
    if (runStatus) { runStatus.className = 'run-status idle'; }
    if (feedbackBox) feedbackBox.style.display = 'none';

    /* Reset all test statuses */
    document.querySelectorAll('.test-status').forEach(el => {
      el.className = 'test-status pending';
      el.textContent = '';
    });
  },

  /* ── Execute Python code via Pyodide ─────────────────────────── */
  async _runCode(lesson) {
    const runBtn  = document.getElementById('lesson-run-btn');
    const ex      = LessonPage._currentExercise;
    if (!ex) return;

    const code = LessonPage._monacoInstance?.getValue() || '';

    runBtn.textContent = '⏳';
    runBtn.disabled    = true;

    LessonPage._setRunStatus('loading', 'Ejecutando...');

    try {
      const result = await PythonRunner.run(code);
      LessonPage._displayResult(result, ex);
    } catch(err) {
      LessonPage._setRunStatus('error', 'Error inesperado al ejecutar');
    } finally {
      runBtn.textContent = '▶ Ejecutar';
      runBtn.disabled    = false;
    }
  },

  _displayResult(result, exercise) {
    /* Show terminal output */
    const termContainer = document.getElementById('terminal-output-container');
    const termEl        = document.getElementById('terminal-output');
    const feedbackBox   = document.getElementById('feedback-box');

    if (result.output && result.output.trim()) {
      if (termContainer) termContainer.style.display = 'block';
      if (termEl) termEl.textContent = result.output;
    }

    if (!result.success) {
      const errType = result.errorType || 'default';
      const pedMsg  = SKILLOGIC_DATA.errorFeedback[errType] || SKILLOGIC_DATA.errorFeedback.default;

      LessonPage._setRunStatus('error', 'Error en el código');

      if (feedbackBox) {
        feedbackBox.style.display = 'block';
        feedbackBox.innerHTML = `<strong>❌ ${errType || 'Error'}:</strong> ${pedMsg}`;
      }
      return;
    }

    /* Evaluate tests */
    let allPass = true;

    exercise.tests.forEach(test => {
      const pass = test.check(result.output);
      if (!pass) allPass = false;

      /* Find the status dot for this test */
      const key = `${exercise.id}_${test.description}`;
      const dot = document.querySelector(`.test-status[data-test="${key}"]`);
      if (dot) {
        dot.className = `test-status ${pass ? 'pass' : 'fail'}`;
        dot.textContent = pass ? '✓' : '✗';
      }
    });

    if (allPass) {
      LessonPage._setRunStatus('success', `¡Correcto! +${exercise.xp} XP 🎉`);

      const lessonSlug = AppState.get().currentLesson?.slug || '';
      const isNew = AppState.markExerciseComplete(lessonSlug, exercise.id, exercise.xp);

      if (isNew) {
        Toast.show(`¡Ejercicio completado! +${exercise.xp} XP 🎉`, 'success');

        /* Update exercise button icon */
        const btn = document.getElementById(`ex-btn-${exercise.id}`);
        if (btn) {
          const iconEl = btn.querySelector('.flex span:first-child');
          if (iconEl) iconEl.textContent = '✅';
        }
      }
    } else {
      LessonPage._setRunStatus('error', 'Algunos tests fallaron. ¡Sigue intentando!');
    }
  },

  _setRunStatus(type, message) {
    const el = document.getElementById('run-status');
    if (!el) return;
    el.className = `run-status ${type}`;
    const icons = { loading: '⏳', success: '✅', error: '❌', 'python-loading': '🐍' };
    el.innerHTML = `<span>${icons[type] || ''}</span> <span>${message}</span>`;
  },
};
