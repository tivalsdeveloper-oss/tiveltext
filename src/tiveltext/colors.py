"""ANSI foreground/background color helpers."""
import re

NAMED = {
    "black": 30, "red": 31, "green": 32, "yellow": 33, "blue": 34,
    "magenta": 35, "cyan": 36, "white": 37,
    "bright_black": 90, "bright_red": 91, "bright_green": 92,
    "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
    "bright_cyan": 96, "bright_white": 97,
}
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

def _rgb(value):
    if isinstance(value, (tuple, list)) and len(value) == 3:
        return tuple(max(0, min(255, int(x))) for x in value)
    if isinstance(value, str) and value.startswith("#") and len(value) == 7:
        try:
            return tuple(int(value[i:i+2], 16) for i in (1, 3, 5))
        except ValueError:
            return None
    return None

def ansi(color=None, background=None, bold=False, underline=False):
    codes = []
    if bold: codes.append("1")
    if underline: codes.append("4")
    rgb = _rgb(color)
    if rgb: codes.append(f"38;2;{rgb[0]};{rgb[1]};{rgb[2]}")
    elif color:
        key = str(color).lower()
        if key not in NAMED: raise ValueError(f"Unknown color: {color}")
        codes.append(str(NAMED[key]))
    bg = _rgb(background)
    if bg: codes.append(f"48;2;{bg[0]};{bg[1]};{bg[2]}")
    elif background:
        key = str(background).lower()
        if key not in NAMED: raise ValueError(f"Unknown background: {background}")
        codes.append(str(NAMED[key] + 10))
    return f"\033[{';'.join(codes)}m" if codes else ""

def colorize(value, color=None, background=None, bold=False, underline=False):
    prefix = ansi(color, background, bold, underline)
    return f"{prefix}{value}\033[0m" if prefix else str(value)

def strip_ansi(value):
    return ANSI_RE.sub("", str(value))
