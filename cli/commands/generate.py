from cli.generators import drawable
from cli.generators import appfilter

NAME = "generate"
HELP = "Gera arquivos do icon pack"

def register(subparsers):
    parser = subparsers.add_parser(NAME, help=HELP)
    actions = parser.add_subparsers(dest="generate_command", required=True)

    p = actions.add_parser("drawable", help="Gera drawable.xml")
    p.set_defaults(func=lambda args: drawable.generate())

    p = actions.add_parser("appfilter", help="Gera appfilter.xml")
    p.set_defaults(func=lambda args: appfilter.generate())
