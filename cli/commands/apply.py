from cli.android.importer import run as importer
from cli.commands.scan import run as scan
from cli.commands.generate import generate_all
from cli.android.build import build
from cli.commands.install import run as install

NAME = "apply"
HELP = "Importa um ícone e executa o pipeline completo"

def register(sub):
    p = sub.add_parser(NAME, help=HELP)
    p.add_argument("name")
    p.set_defaults(func=run)

def run(args):
    print(f"🍬 Aplicando {args.name}")

    try:
        print("\n📥 Importando")
        importer(args.name)

        print("\n🔍 Sincronizando")
        scan(None)

        print("\n⚙️ Gerando")
        generate_all()

        print("\n🔨 Compilando")
        build()

        print("\n📦 Instalando")
        install(None)

        print("\n✅ Apply concluído")

    except RuntimeError as e:
        print(f"\n❌ {e}")
        print("⛔ Apply interrompido.")
        raise SystemExit(1)
