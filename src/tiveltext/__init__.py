"""TivelText: stylized terminal text, colors, backgrounds, and effects."""
from .core import text, fonts
from .colors import (
    color, colorize, color_list, color_dict, color_object,
    rgb, hex, rainbow, gradient, strip_ansi, supports_color,
)
from .styles import TextStyle, style
from .decorators import decorate, decorations

__version__ = "1.1.0.dev0"
__all__ = [
    "text", "fonts", "color", "colorize", "color_list", "color_dict",
    "color_object", "rgb", "hex", "rainbow", "gradient", "strip_ansi",
    "supports_color", "TextStyle", "style", "decorate", "decorations",
]
