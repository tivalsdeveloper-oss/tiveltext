# TivelText 1.0.0

**Turn ordinary words into extraordinary text.**

TivelText is a zero-runtime-dependency Python library for ASCII-art text, Unicode typography, decorative boxes, ANSI foreground/background colors, and a terminal CLI.

## Install

```bash
python -m pip install tiveltext
```

## Python

```python
from tiveltext import text, decorate

print(text("TIVALS", font="block"))
print(text("TivelText", font="gothic", color="cyan"))
print(text("Developer", font="script"))
print(text("TIVALS", font="block", color="#00ffff", background="#111111"))
print(decorate("TivelText", "double"))
```

## Built-in styles

ASCII: `block`, `banner`, `big`, `bubble`, `digital`, `shadow`, `slant`, `small`.

Unicode: `bold`, `italic`, `script`, `gothic`, `double`, `monospace`, `fullwidth`, `smallcaps`, `circled`, `squared`.

Decorations: `box`, `square`, `double`, `stars`, `brackets`, `arrows`.

List styles programmatically:

```python
from tiveltext import fonts
print(fonts())
```

## CLI

```bash
tiveltext "TIVALS" --font block
tiveltext "TivelText" --font gothic --color cyan
tiveltext "TIVALS" --font block --color "#00ffff" --background "#111111"
tiveltext "TivelText" --font block --decoration double
tiveltext --list-fonts
```

Use `--plain` to disable ANSI styling.

## Development

```bash
python -m pip install -e .
python -m pytest
python -m build
```

## License

MIT License. Copyright (c) 2026 Tivalsdeveloper.
