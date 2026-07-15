from cli.android.importer import run as importer

NAME="icon"
HELP="Gerencia ícones"

def register(sub):
    p=sub.add_parser(NAME,help=HELP)
    s=p.add_subparsers(dest="action",required=True)

    i=s.add_parser("import",help="Importa metadados")
    i.add_argument("name")
    i.set_defaults(func=lambda a: importer(a.name))
