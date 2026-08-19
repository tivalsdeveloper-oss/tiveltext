"""Decorative text wrappers."""
_DECORATIONS = {
    "box": ("╭","╰","╮","╯","─","│"),
    "square": ("┌","└","┐","┘","─","│"),
    "double": ("╔","╚","╗","╝","═","║"),
    "stars": ("✦","✦","✦","✦","─"," "),
    "brackets": ("[","[","]","]"," "," "),
    "arrows": ("➤","➤","➤","➤","─"," "),
}

def decorations(): return sorted(_DECORATIONS)

def decorate(value, style="box", padding=1):
    if style not in _DECORATIONS: raise ValueError(f"Unknown decoration '{style}'")
    tl, bl, tr, br, h, v = _DECORATIONS[style]
    lines = str(value).splitlines() or [""]
    width = max(map(len, lines))
    inner = width + padding * 2
    top, bottom = tl + h*inner + tr, bl + h*inner + br
    body = [v + ' '*padding + line.ljust(width) + ' '*padding + v for line in lines]
    return '\n'.join([top, *body, bottom])
