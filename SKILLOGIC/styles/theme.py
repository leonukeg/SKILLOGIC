"""
SKILLOGIC — Design Tokens
Single source of truth for all visual constants.
Never use magic numbers or hardcoded colors in components.
"""

# ── Backgrounds ────────────────────────────────────────────────
BG_PRIMARY    = "#0D1117"
BG_SECONDARY  = "#161B22"
BG_ELEVATED   = "#1C2128"
BG_HOVER      = "#21262D"

# ── Borders ────────────────────────────────────────────────────
BORDER        = "#30363D"
BORDER_SUBTLE = "#21262D"
BORDER_STRONG = "#484F58"

# ── Text ───────────────────────────────────────────────────────
TEXT_PRIMARY   = "#E6EDF3"
TEXT_SECONDARY = "#8B949E"
TEXT_MUTED     = "#656D76"
TEXT_DISABLED  = "#3D444D"

# ── Brand (Purple) ─────────────────────────────────────────────
BRAND        = "#7C3AED"
BRAND_HOVER  = "#6D28D9"
BRAND_ACTIVE = "#5B21B6"
BRAND_LIGHT  = "rgba(124, 58, 237, 0.12)"
BRAND_MEDIUM = "rgba(124, 58, 237, 0.25)"
BRAND_GLOW   = "rgba(124, 58, 237, 0.40)"

# ── Semantic ───────────────────────────────────────────────────
SUCCESS       = "#2EA043"
SUCCESS_LIGHT = "rgba(46, 160, 67, 0.12)"
WARNING       = "#D29922"
WARNING_LIGHT = "rgba(210, 153, 34, 0.12)"
ERROR         = "#F85149"
ERROR_LIGHT   = "rgba(248, 81, 73, 0.12)"
INFO          = "#388BFD"
INFO_LIGHT    = "rgba(56, 139, 253, 0.12)"

# ── Streak (Orange) ────────────────────────────────────────────
STREAK       = "#F97316"
STREAK_LIGHT = "rgba(249, 115, 22, 0.12)"
STREAK_GLOW  = "rgba(249, 115, 22, 0.35)"

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

# ── Shadows ────────────────────────────────────────────────────
SHADOW_XS    = "0 1px 2px rgba(0,0,0,0.35)"
SHADOW_SM    = "0 1px 4px rgba(0,0,0,0.40)"
SHADOW_MD    = "0 4px 12px rgba(0,0,0,0.45)"
SHADOW_LG    = "0 8px 24px rgba(0,0,0,0.55)"
SHADOW_XL    = "0 16px 48px rgba(0,0,0,0.65)"
SHADOW_BRAND = "0 4px 24px rgba(124, 58, 237, 0.40)"
SHADOW_STREAK= "0 4px 20px rgba(249, 115, 22, 0.35)"

# ── Transitions ────────────────────────────────────────────────
EASE_FAST   = "120ms ease"
EASE_BASE   = "220ms ease"
EASE_SLOW   = "380ms ease"
EASE_BOUNCE = "350ms cubic-bezier(0.34, 1.56, 0.64, 1)"

# ── Layout Dimensions ──────────────────────────────────────────
SIDEBAR_WIDTH      = "220px"
TOPBAR_HEIGHT      = "60px"
RIGHT_PANEL_WIDTH  = "280px"

# ── Levels ─────────────────────────────────────────────────────
LEVELS = [
    {"level": 1, "name": "Aprendiz",    "xp_required": 0},
    {"level": 2, "name": "Iniciado",    "xp_required": 500},
    {"level": 3, "name": "Practicante", "xp_required": 1000},
    {"level": 4, "name": "Avanzado",    "xp_required": 1500},
    {"level": 5, "name": "Maestro",     "xp_required": 2500},
]

# ── Stylesheet URL (Google Fonts) ──────────────────────────────
GOOGLE_FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Inter:wght@300;400;500;600;700;800;900&"
    "family=JetBrains+Mono:ital,wght@0,400;0,500;0,600;1,400&"
    "display=swap"
)

# ── Light theme overrides ──────────────────────────────────────
LIGHT = {
    "BG_PRIMARY":    "#FFFFFF",
    "BG_SECONDARY":  "#F6F8FA",
    "BG_ELEVATED":   "#EAEEF2",
    "BG_HOVER":      "#EFF1F3",
    "BORDER":        "#D0D7DE",
    "BORDER_SUBTLE": "#EAEEF2",
    "BORDER_STRONG": "#8C959F",
    "TEXT_PRIMARY":   "#1F2328",
    "TEXT_SECONDARY": "#57606A",
    "TEXT_MUTED":     "#6E7781",
    "TEXT_DISABLED":  "#AFB8C1",
}
