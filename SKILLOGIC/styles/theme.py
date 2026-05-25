"""
SKILLOGIC — Design Tokens
Single source of truth for all visual constants.

Color tokens use CSS custom property references (var(--token)).
This makes the dark/light theme switch work automatically:
  - The wrapper element carries data-theme="dark|light"
  - assets/theme.css defines var values for each theme
  - Components use these constants → valid CSS var() references

Non-color tokens (spacing, typography, layout) are plain values.
"""

# ── Backgrounds ────────────────────────────────────────────────
BG_PRIMARY    = "var(--bg-primary)"
BG_SECONDARY  = "var(--bg-secondary)"
BG_ELEVATED   = "var(--bg-elevated)"
BG_HOVER      = "var(--bg-hover)"

# ── Borders ────────────────────────────────────────────────────
BORDER        = "var(--border)"
BORDER_SUBTLE = "var(--border-subtle)"
BORDER_STRONG = "var(--border-strong)"

# ── Text ───────────────────────────────────────────────────────
TEXT_PRIMARY   = "var(--text-primary)"
TEXT_SECONDARY = "var(--text-secondary)"
TEXT_MUTED     = "var(--text-muted)"
TEXT_DISABLED  = "var(--text-disabled)"

# ── Brand (purple) ─────────────────────────────────────────────
BRAND        = "var(--brand)"
BRAND_HOVER  = "var(--brand-hover)"
BRAND_ACTIVE = "var(--brand-active)"
BRAND_LIGHT  = "var(--brand-light)"
BRAND_MEDIUM = "var(--brand-medium)"
BRAND_GLOW   = "var(--brand-glow)"

# ── Semantic ───────────────────────────────────────────────────
SUCCESS       = "var(--success)"
SUCCESS_LIGHT = "var(--success-light)"
WARNING       = "var(--warning)"
WARNING_LIGHT = "var(--warning-light)"
ERROR         = "var(--error)"
ERROR_LIGHT   = "var(--error-light)"
INFO          = "var(--info)"
INFO_LIGHT    = "var(--info-light)"

# ── Streak (orange) ────────────────────────────────────────────
STREAK        = "var(--streak)"
STREAK_LIGHT  = "var(--streak-light)"
STREAK_GLOW   = "var(--streak-glow)"

# ── Shadows ────────────────────────────────────────────────────
SHADOW_XS     = "var(--shadow-xs)"
SHADOW_SM     = "var(--shadow-sm)"
SHADOW_MD     = "var(--shadow-md)"
SHADOW_LG     = "var(--shadow-lg)"
SHADOW_XL     = "var(--shadow-xl)"
SHADOW_BRAND  = "var(--shadow-brand)"
SHADOW_STREAK = "var(--shadow-streak)"

# ── Hero card ──────────────────────────────────────────────────
HERO_GRADIENT = "var(--hero-gradient)"
HERO_BORDER   = "var(--hero-border)"
HERO_TEXT     = "var(--hero-text)"

# ── Code / terminal ────────────────────────────────────────────
CODE_BG   = "var(--code-bg)"
CODE_TEXT = "var(--code-text)"

# ── Input fields ───────────────────────────────────────────────
INPUT_BG   = "var(--input-bg)"
INPUT_TEXT = "var(--input-text)"

# ══════════════════════════════════════════════════════════════
# Non-color tokens — plain values (no theming needed)
# ══════════════════════════════════════════════════════════════

# ── Typography ─────────────────────────────────────────────────
FONT_BODY = "'Inter', system-ui, -apple-system, sans-serif"
FONT_CODE = "'JetBrains Mono', 'Fira Code', monospace"

# ── Font Sizes ─────────────────────────────────────────────────
TEXT_XS   = "11px"
TEXT_SM   = "13px"
TEXT_BASE = "14px"
TEXT_MD   = "15px"
TEXT_LG   = "18px"
TEXT_XL   = "22px"
TEXT_2XL  = "28px"
TEXT_3XL  = "36px"
TEXT_4XL  = "48px"

# ── Font Weights ───────────────────────────────────────────────
WEIGHT_NORMAL    = "400"
WEIGHT_MEDIUM    = "500"
WEIGHT_SEMIBOLD  = "600"
WEIGHT_BOLD      = "700"
WEIGHT_EXTRABOLD = "800"

# ── Spacing ────────────────────────────────────────────────────
SPACE_1  = "4px"
SPACE_2  = "8px"
SPACE_3  = "12px"
SPACE_4  = "16px"
SPACE_5  = "20px"
SPACE_6  = "24px"
SPACE_8  = "32px"
SPACE_10 = "40px"
SPACE_12 = "48px"
SPACE_16 = "64px"

# ── Border Radius ──────────────────────────────────────────────
RADIUS_XS   = "4px"
RADIUS_SM   = "6px"
RADIUS_MD   = "10px"
RADIUS_LG   = "14px"
RADIUS_XL   = "20px"
RADIUS_2XL  = "28px"
RADIUS_FULL = "9999px"

# ── Transitions ────────────────────────────────────────────────
EASE_FAST   = "120ms ease"
EASE_BASE   = "220ms ease"
EASE_SLOW   = "380ms ease"
EASE_BOUNCE = "350ms cubic-bezier(0.34, 1.56, 0.64, 1)"

# ── Layout Dimensions ──────────────────────────────────────────
SIDEBAR_WIDTH     = "220px"
TOPBAR_HEIGHT     = "60px"
RIGHT_PANEL_WIDTH = "280px"

# ── Level definitions (data, not CSS) ──────────────────────────
LEVELS = [
    {"level": 1, "name": "Aprendiz",    "xp_required": 0},
    {"level": 2, "name": "Iniciado",    "xp_required": 500},
    {"level": 3, "name": "Practicante", "xp_required": 1000},
    {"level": 4, "name": "Avanzado",    "xp_required": 1500},
    {"level": 5, "name": "Maestro",     "xp_required": 2500},
]

# ── Google Fonts URL ───────────────────────────────────────────
GOOGLE_FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Inter:wght@300;400;500;600;700;800;900&"
    "family=JetBrains+Mono:ital,wght@0,400;0,500;0,600;1,400&"
    "display=swap"
)

# ── Accent colors (decorative, same in both themes) ────────────
# Used for gradients and accents — not in the theme system
ACCENT_VIOLET = "#a855f7"
ACCENT_LILAC  = "#a78bfa"
