from pathlib import Path
import shutil

NAME = "icon"
HELP = "Gerencia ícones"

def import_icon(args):
    source = Path.home() / "storage/shared/Download" / f"{args.name}.png"
    target = Path("assets/pixelart/originals") / f"{args.name}.png"

    if not source.exists():
        print(f"❌ Arquivo não encontrado: {source}")
        return

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)

    print(f"✅ {target} importado.")

def register(subparsers):
    parser = subparsers.add_parser(NAME, help=HELP)

    actions = parser.add_subparsers(
        dest="icon_command",
        required=True,
    )

    imp = actions.add_parser(
        "import",
        help="Importa um PNG da pasta Download",
    )

    imp.add_argument("name")
    imp.set_defaults(func=import_icon)
