import argparse
import json
from pathlib import Path

from cli.metadata import VERSION
from cli.commands import COMMANDS

def dashboard():
    icons = 0
    db = Path("assets/database/icons.json")

    if db.exists():
        try:
            icons = len(json.loads(db.read_text(encoding="utf-8"))["icons"])
        except Exception:
            pass

    print(f"🍬 MiniCandy SDK v{VERSION}")
    print()
    print("Projeto")
    print("──────────────")
    print(f"Ícones............... {icons}")
    print(f"Banco................ {'OK' if db.exists() else '--'}")
    print(f"Drawable............. {'OK' if Path('app/src/main/res/xml/drawable.xml').exists() else '--'}")
    print(f"AppFilter............ {'OK' if Path('app/src/main/res/xml/appfilter.xml').exists() else '--'}")
    print()
    print("Comandos")
    print("──────────────")
    for name in sorted(COMMANDS):
        print(f"  {name}")

def main():
    parser = argparse.ArgumentParser(prog="mc")
    parser.add_argument(
        "--version",
        action="version",
        version=f"MiniCandy {VERSION}"
    )

    sub = parser.add_subparsers(dest="command")

    for module in COMMANDS.values():
        if hasattr(module, "register"):
            module.register(sub)
        else:
            p = sub.add_parser(module.NAME, help=module.HELP)
            p.set_defaults(func=module.run)

    args, unknown = parser.parse_known_args()
    args._unknown = unknown

    if args.command is None:
        dashboard()
        return

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
