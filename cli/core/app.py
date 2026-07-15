import argparse
from cli.core.registry import load
from cli.commands.icon.import_cmd import run as icon_import
from cli.metadata import VERSION

def main():
    parser = argparse.ArgumentParser(prog="mc")
    parser.add_argument("--version", action="version", version=f"MiniCandy {VERSION}")

    sub = parser.add_subparsers(dest="command")

    commands = load()

    for name, module in sorted(commands.items()):
        sub.add_parser(name, help=module.HELP)

    icon = sub.add_parser("icon", help="Gerencia ícones")
    icon_sub = icon.add_subparsers(dest="action")

    imp = icon_sub.add_parser("import", help="Importa um PNG")
    imp.add_argument("name")
    imp.set_defaults(func=icon_import)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    elif args.command in commands:
        commands[args.command].run(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
