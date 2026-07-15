from pathlib import Path
from cli.database.icons import load

def generate():
    icons = load()["icons"]

    xml = [
        '<?xml version="1.0" encoding="utf-8"?>',
        "<resources>",
        "",
    ]

    for icon in icons:
        component = icon.get("component") or "ComponentInfo{}"
        xml.append(f'    <!-- {icon["name"]} -->')
        xml.append(f'    <item component="{component}" drawable="{icon["drawable"]}" />')
        xml.append("")

    xml.append("</resources>")

    out = Path("app/src/main/res/xml/appfilter.xml")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(xml), encoding="utf-8")

    print(f"✅ appfilter.xml ({len(icons)} ícone(s))")
