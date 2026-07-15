from cli.android.detect import detect
from cli.core.console import title

NAME="detect"
HELP="Detecta aplicativos instalados"

def register(subparsers):
    p=subparsers.add_parser(NAME,help=HELP)
    p.add_argument("query",nargs="?",help="Filtro")
    p.add_argument("--activity",action="store_true",help="Mostra launcher activity")
    p.set_defaults(func=run)

def run(args):
    title("MiniCandy Detect")
    detect(args.query,args.activity)
