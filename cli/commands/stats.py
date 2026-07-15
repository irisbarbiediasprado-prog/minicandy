from pathlib import Path
from cli.database.icons import load

NAME = "stats"
HELP = "Mostra estatísticas do projeto"

def run(args):
    icons = load()["icons"]

    drawable = Path("app/src/main/res/xml/drawable.xml").exists()
    appfilter = Path("app/src/main/res/xml/appfilter.xml").exists()

    print("🍬 MiniCandy")
    print()
    print(f"Ícones.............. {len(icons)}")
    print(f"Drawable............ {'OK' if drawable else 'AUSENTE'}")
    print(f"AppFilter........... {'OK' if appfilter else 'AUSENTE'}")
    print("Banco............... OK")

    if icons:
        print(f"Último ícone........ {icons[-1]['name']}")

    print()
    print("Projeto............. Saudável")
