import argparse
from cli.core.registry import load
from cli.metadata import VERSION

def main():
    parser = argparse.ArgumentParser(prog="mc")
    parser.add_argument("--version", action="version", version=f"MiniCandy {VERSION}")

    sub = parser.add_subparsers(dest="command")

    commands = load()

    for name, module in sorted(commands.items()):
        sub.add_parser(name, help=module.HELP)

    args = parser.parse_args()

    if args.command in commands:
        commands[args.command].run(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
