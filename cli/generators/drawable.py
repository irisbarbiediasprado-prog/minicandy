from pathlib import Path
from shutil import copy2
from cli.database.icons import load

SRC = Path("assets/pixelart/originals")
DST = Path("app/src/main/res/drawable-nodpi")

def generate():
    icons = load()["icons"]

    DST.mkdir(parents=True, exist_ok=True)

    for old in DST.glob("*.png"):
        old.unlink()

    xml = [
        '<?xml version="1.0" encoding="utf-8"?>',
        "<resources>",
    ]

    copied = 0

    for icon in icons:
        src = SRC / f'{icon["drawable"]}.png'
        dst = DST / src.name

        if src.exists():
            copy2(src, dst)
            copied += 1

        xml.append(f'    <item drawable="{icon["drawable"]}" />')

    xml.append("</resources>")

    out = Path("app/src/main/res/xml/drawable.xml")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(xml), encoding="utf-8")

    print(f"✅ drawable.xml ({len(icons)} ícone(s))")
    print(f"✅ PNGs copiados: {copied}")
