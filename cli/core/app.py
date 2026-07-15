import argparse

from cli.metadata import VERSION

from cli.commands import doctor
from cli.commands import version
from cli.commands import generate
from cli.commands import icon

COMMANDS = {
    doctor.NAME: doctor,
    version.NAME: version,
    generate.NAME: generate,
    icon.NAME: icon,
}

def main():
    parser = argparse.ArgumentParser(prog="mc")
    parser.add_argument(
        "--version",
        action="version",
        version=f"MiniCandy {VERSION}"
    )

    sub = parser.add_subparsers(dest="command")

    for module in COMMANDS.values():
        p = sub.add_parser(module.NAME, help=module.HELP)
        p.set_defaults(func=module.run)

    args, unknown = parser.parse_known_args()
    args._unknown = unknown

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
