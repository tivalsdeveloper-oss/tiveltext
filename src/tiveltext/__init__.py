"""TivelText 1.0.0: stylized text and ASCII art for Python."""
from .core import text, fonts
from .colors import colorize, strip_ansi
from .decorators import decorate, decorations

__version__ = "1.0.0"
__all__ = ["text", "fonts", "colorize", "strip_ansi", "decorate", "decorations"]
