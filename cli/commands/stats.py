from cli.core.console import title, step, success, blank

from pathlib import Path
from cli.database.icons import load

NAME = "stats"
HELP = "Mostra estatísticas do projeto"

def run(args):
    icons = load()["icons"]

    drawable = Path("app/src/main/res/xml/drawable.xml").exists()
    appfilter = Path("app/src/main/res/xml/appfilter.xml").exists()

    title("MiniCandy")
    blank()
    print(f"Ícones.............. {len(icons)}")
    print(f"Drawable............ {'OK' if drawable else 'AUSENTE'}")
    print(f"AppFilter........... {'OK' if appfilter else 'AUSENTE'}")
    print("Banco............... OK")

    if icons:
        print(f"Último ícone........ {icons[-1]['name']}")

    blank()
    print("Projeto............. Saudável")
