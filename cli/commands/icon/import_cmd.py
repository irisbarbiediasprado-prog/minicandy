from pathlib import Path
import shutil
from cli.utils.image import validate_png

def run(args):
    source = Path.home() / "storage/shared/Download" / f"{args.name}.png"

    ok, message = validate_png(source)

    if not ok:
        print("❌", message)
        return

    target = Path("assets/pixelart/originals")
    target.mkdir(parents=True, exist_ok=True)

    shutil.copy2(source, target / source.name)

    print("🍬 MiniCandy\n")
    print("✔ PNG")
    print("✔ 512x512")
    print("✔ Transparência")
    print()
    print("✅ Importado:", source.name)
