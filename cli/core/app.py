import argparse

from cli.metadata import VERSION
from cli.core.registry import load

def main():
    parser = argparse.ArgumentParser(prog="mc")
    parser.add_argument(
        "--version",
        action="version",
        version=f"MiniCandy {VERSION}"
    )

    subparsers = parser.add_subparsers(dest="command")

    commands = load()

    for name, module in commands.items():
        cmd = subparsers.add_parser(name, help=module.HELP)
        cmd.set_defaults(handler=module.run)

    args = parser.parse_args()

    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()
