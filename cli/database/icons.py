import json
from pathlib import Path

DB = Path("assets/database/icons.json")
ICONS_DIR = Path("assets/pixelart/originals")

def rebuild():
    icons = []

    if ICONS_DIR.exists():
        for png in sorted(ICONS_DIR.glob("*.png")):
            icons.append({
                "name": png.stem,
                "drawable": png.stem,
                "file": str(png).replace("\\", "/")
            })

    DB.parent.mkdir(parents=True, exist_ok=True)

    DB.write_text(
        json.dumps(
            {"icons": icons},
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    print(f"✅ Banco atualizado: {len(icons)} ícone(s)")
