from pathlib import Path
import shutil

NAME = "icon"
HELP = "Importa ícones"

def run(args):
    unknown = getattr(args, "_unknown", [])

    if len(unknown) != 2 or unknown[0] != "import":
        print("Uso:")
        print("  mc icon import <nome>")
        return

    name = unknown[1]

    source = Path.home() / "storage/shared/Download" / f"{name}.png"
    target = Path("assets/pixelart/originals") / f"{name}.png"

    if not source.exists():
        print(f"❌ Arquivo não encontrado: {source}")
        return

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)

    print(f"✅ {target} importado.")
