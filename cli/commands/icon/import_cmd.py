from pathlib import Path
import shutil

NAME = "icon"
HELP = "Gerencia ícones"

def run(args):
    if not args.name:
        print("Uso: mc icon import <nome>")
        return

    source = Path.home() / "storage/shared/Download" / f"{args.name}.png"
    target_dir = Path("assets/pixelart/originals")
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / source.name

    if not source.exists():
        print(f"❌ Arquivo não encontrado: {source}")
        return

    shutil.copy2(source, target)

    print("✅ Ícone importado")
    print(target)
