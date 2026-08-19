"""Chainable text styling for TivelText."""
from .colors import ansi

class TextStyle:
    """Build a styled terminal string with a fluent API."""
    def __init__(self, value=""):
        self.value = str(value)
        self._color = None
        self._background = None
        self._bold = False
        self._underline = False
        self._italic = False
        self._dim = False
        self._reverse = False
        self._strike = False

    def color(self, value): self._color = value; return self
    def bg(self, value): self._background = value; return self
    def background(self, value): return self.bg(value)
    def rgb(self, r, g, b): self._color = (r, g, b); return self
    def bg_rgb(self, r, g, b): self._background = (r, g, b); return self
    def hex(self, value): self._color = value; return self
    def bg_hex(self, value): self._background = value; return self
    def bold(self): self._bold = True; return self
    def underline(self): self._underline = True; return self
    def italic(self): self._italic = True; return self
    def dim(self): self._dim = True; return self
    def reverse(self): self._reverse = True; return self
    def strikethrough(self): self._strike = True; return self

    def build(self):
        codes = []
        if self._bold: codes.append("1")
        if self._dim: codes.append("2")
        if self._italic: codes.append("3")
        if self._underline: codes.append("4")
        if self._reverse: codes.append("7")
        if self._strike: codes.append("9")
        prefix = ansi(self._color, self._background)
        if codes:
            extra = f"\033[{';'.join(codes)}m"
            prefix = extra + prefix
        return f"{prefix}{self.value}\033[0m" if prefix else self.value

    def __str__(self): return self.build()
    def __repr__(self): return self.build()

def style(value=""):
    return TextStyle(value)
