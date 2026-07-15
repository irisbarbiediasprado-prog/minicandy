from pathlib import Path
from cli.database.icons import load

def generate():
    icons = load()["icons"]

    xml = [
        '<?xml version="1.0" encoding="utf-8"?>',
        "<resources>",
    ]

    for icon in icons:
        xml.append(f'    <item drawable="{icon["drawable"]}" />')

    xml.append("</resources>")

    out = Path("app/src/main/res/xml/drawable.xml")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(xml), encoding="utf-8")

    print(f"✅ drawable.xml ({len(icons)} ícone(s))")
