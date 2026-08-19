"""TivelText command-line interface."""
import argparse
from .core import text, fonts
from .decorators import decorate, decorations

def main(argv=None):
    p = argparse.ArgumentParser(prog="tiveltext", description="Turn ordinary words into extraordinary text.")
    p.add_argument("value", nargs="*", help="Text to render")
    p.add_argument("--font", default="block")
    p.add_argument("--color")
    p.add_argument("--background")
    p.add_argument("--decoration", choices=decorations())
    p.add_argument("--plain", action="store_true")
    p.add_argument("--list-fonts", action="store_true")
    p.add_argument("--list-decorations", action="store_true")
    args = p.parse_args(argv)
    if args.list_fonts:
        print('\n'.join(fonts())); return 0
    if args.list_decorations:
        print('\n'.join(decorations())); return 0
    if not args.value:
        p.print_help(); return 0
    result = text(' '.join(args.value), args.font, args.color, args.background, plain=args.plain)
    if args.decoration: result = decorate(result, args.decoration)
    print(result); return 0

if __name__ == "__main__": raise SystemExit(main())
