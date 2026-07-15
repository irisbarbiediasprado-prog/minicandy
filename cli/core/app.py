import argparse

from cli.metadata import VERSION

from cli.commands import doctor
from cli.commands import version
from cli.commands import generate
from cli.commands import icon
from cli.commands import scan

MODULES = (
    doctor,
    version,
    generate,
    icon,
    scan,
)

def main():
    parser = argparse.ArgumentParser(prog="mc")

    parser.add_argument(
        "--version",
        action="version",
        version=f"MiniCandy {VERSION}",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    for module in MODULES:
        if hasattr(module, "register"):
            module.register(subparsers)
        else:
            p = subparsers.add_parser(module.NAME, help=module.HELP)
            p.set_defaults(func=module.run)

    args = parser.parse_args()

    args.func(args)

if __name__ == "__main__":
    main()
