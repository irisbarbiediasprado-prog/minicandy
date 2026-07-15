from pathlib import Path

NAME = "clean"
HELP = "Remove artefatos gerados"

FILES = [
    Path("assets/database/icons.json"),
    Path("app/src/main/res/xml/drawable.xml"),
    Path("app/src/main/res/xml/appfilter.xml"),
]

def run(args):
    print("🧹 MiniCandy Clean")
    print()

    removed = 0

    for file in FILES:
        if file.exists():
            file.unlink()
            print(f"✔ Removido: {file}")
            removed += 1

    if removed == 0:
        print("Nada para limpar.")
    else:
        print()
        print(f"✅ {removed} arquivo(s) removido(s).")
