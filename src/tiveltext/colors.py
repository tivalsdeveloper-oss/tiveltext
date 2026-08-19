"""ANSI color, background, RGB/HEX, recursive value, and terminal helpers."""
import os
import re
import sys
from collections.abc import Mapping

RESET = "\033[0m"
NAMED = {
    "black": 30, "red": 31, "green": 32, "yellow": 33,
    "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
    "bright_black": 90, "bright_red": 91, "bright_green": 92,
    "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
    "bright_cyan": 96, "bright_white": 97,
}
STYLES = {"bold": 1, "dim": 2, "italic": 3, "underline": 4,
          "blink": 5, "reverse": 7, "hidden": 8, "strikethrough": 9}
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def supports_color(stream=None):
    """Return whether ANSI color should normally be emitted."""
    stream = stream or sys.stdout
    if os.environ.get("NO_COLOR") is not None or os.environ.get("TERM") == "dumb":
        return False
    return bool(getattr(stream, "isatty", lambda: False)())


def _rgb(value):
    if isinstance(value, (tuple, list)) and len(value) == 3:
        try:
            values = tuple(int(x) for x in value)
        except (TypeError, ValueError):
            raise ValueError("RGB values must be integers")
        if not all(0 <= x <= 255 for x in values):
            raise ValueError("RGB values must be between 0 and 255")
        return values
    if isinstance(value, str):
        value = value.strip()
        if re.fullmatch(r"#[0-9a-fA-F]{6}", value):
            return tuple(int(value[i:i + 2], 16) for i in (1, 3, 5))
        if re.fullmatch(r"#[0-9a-fA-F]{3}", value):
            return tuple(int(c * 2, 16) for c in value[1:])
    return None


def ansi(color=None, background=None, bold=False, underline=False, **styles):
    """Build an ANSI prefix from named, RGB, or HEX colors and styles."""
    codes = []
    enabled = {"bold": bold, "underline": underline, **styles}
    for name, active in enabled.items():
        if active:
            if name not in STYLES:
                raise ValueError(f"Unknown text style: {name}")
            codes.append(str(STYLES[name]))

    rgb = _rgb(color)
    if rgb:
        codes.append(f"38;2;{rgb[0]};{rgb[1]};{rgb[2]}")
    elif color:
        key = str(color).lower()
        if key not in NAMED:
            raise ValueError(f"Unknown color: {color}")
        codes.append(str(NAMED[key]))

    bg = _rgb(background)
    if bg:
        codes.append(f"48;2;{bg[0]};{bg[1]};{bg[2]}")
    elif background:
        key = str(background).lower()
        if key not in NAMED:
            raise ValueError(f"Unknown background: {background}")
        codes.append(str(NAMED[key] + 10))
    return f"\033[{';'.join(codes)}m" if codes else ""


def colorize(value, color=None, background=None, bold=False, underline=False,
             italic=False, dim=False, reverse=False, strikethrough=False,
             recursive=False, force=True):
    """Color any Python value; recursively style lists, tuples, sets and dicts."""
    if recursive:
        if isinstance(value, Mapping):
            return {k: colorize(v, color, background, bold, underline, italic,
                                 dim, reverse, strikethrough, True, force)
                    for k, v in value.items()}
        if isinstance(value, (list, tuple, set)):
            converted = [colorize(v, color, background, bold, underline, italic,
                                  dim, reverse, strikethrough, True, force)
                         for v in value]
            return type(value)(converted) if not isinstance(value, set) else set(converted)
    prefix = ansi(color, background, bold, underline, italic=italic, dim=dim,
                  reverse=reverse, strikethrough=strikethrough)
    if not force and not supports_color():
        prefix = ""
    return f"{prefix}{value}{RESET}" if prefix else str(value)


def color(value, fg=None, bg=None, **kwargs):
    """Short alias for colorize(value, fg, bg). Works naturally with f-strings."""
    return colorize(value, color=fg, background=bg, **kwargs)


def rgb(value, r, g, b, **kwargs):
    return colorize(value, color=(r, g, b), **kwargs)


def hex(value, color_code, **kwargs):
    return colorize(value, color=color_code, **kwargs)


def color_list(values, color=None, background=None, **kwargs):
    """Return a new list with each element styled."""
    return [colorize(v, color, background, **kwargs) for v in values]


def color_dict(mapping, key_color=None, value_color=None, **kwargs):
    """Return a dictionary with independently styled keys and values."""
    return {colorize(k, key_color, **kwargs): colorize(v, value_color, **kwargs)
            for k, v in mapping.items()}


def color_object(obj, attributes=None, color=None, background=None, **kwargs):
    """Style selected public object attributes as a dictionary."""
    names = attributes or [n for n in vars(obj) if not n.startswith("_")]
    return {name: colorize(getattr(obj, name), color, background, **kwargs)
            for name in names}


def strip_ansi(value):
    return ANSI_RE.sub("", str(value))


def rainbow(value):
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    return "".join(color(ch, colors[i % len(colors)]) for i, ch in enumerate(str(value)))


def gradient(value, start_color, end_color):
    value = str(value)
    start, end = _rgb(start_color), _rgb(end_color)
    if not start or not end:
        raise ValueError("Gradient colors must be RGB tuples/lists or HEX strings")
    result = []
    length = max(len(value) - 1, 1)
    for i, ch in enumerate(value):
        ratio = i / length
        rgb_value = tuple(round(start[j] + (end[j] - start[j]) * ratio) for j in range(3))
        result.append(color(ch, fg=rgb_value))
    return "".join(result)
