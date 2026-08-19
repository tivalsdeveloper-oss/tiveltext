"""Main TivelText API."""
from .registry import get_font, list_fonts
from .unicode import transform
from .colors import colorize

_UNICODE = {"bold","italic","script","gothic","double","monospace","fullwidth","smallcaps","circled","squared"}

def fonts():
    return list_fonts()

def text(value, font="block", color=None, background=None, bold=False, underline=False, plain=False):
    value = str(value)
    rendered = transform(value, font) if font.lower() in _UNICODE else get_font(font)(value)
    return rendered if plain else colorize(rendered, color, background, bold, underline)
