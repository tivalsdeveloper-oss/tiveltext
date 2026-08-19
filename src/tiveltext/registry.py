"""Font registry."""
from ._ascii import make_ascii_module

_ASCII = {name: make_ascii_module(name) for name in ("block","banner","big","bubble","digital","shadow","slant","small")}
_UNICODE = {"bold","italic","script","gothic","double","monospace","fullwidth","smallcaps","circled","squared"}

def list_fonts():
    return sorted((*_ASCII.keys(), *_UNICODE))

def get_font(name):
    key = str(name).lower()
    if key in _ASCII: return _ASCII[key]
    raise ValueError(f"Unknown ASCII font '{name}'. Available: {', '.join(list_fonts())}")
