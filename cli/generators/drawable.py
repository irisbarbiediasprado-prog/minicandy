from pathlib import Path

def generate():
    icons = sorted(Path("assets/pixelart/originals").glob("*.png"))

    xml = [
        '<?xml version="1.0" encoding="utf-8"?>',
        "<resources>",
    ]

    for icon in icons:
        xml.append(f'    <item drawable="{icon.stem}" />')

    xml.append("</resources>")

    out = Path("app/src/main/res/xml/drawable.xml")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(xml), encoding="utf-8")

    print(f"✅ drawable.xml ({len(icons)} ícone(s))")
