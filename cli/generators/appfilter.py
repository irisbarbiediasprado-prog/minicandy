from pathlib import Path

def generate():
    icons = sorted(Path("assets/pixelart/originals").glob("*.png"))

    xml = [
        '<?xml version="1.0" encoding="utf-8"?>',
        "<resources>",
    ]

    for icon in icons:
        xml.append(f'    <!-- TODO: ComponentInfo para {icon.stem} -->')
        xml.append(f'    <item component="ComponentInfo{{}}" drawable="{icon.stem}" />')
        xml.append("")

    xml.append("</resources>")

    out = Path("app/src/main/res/xml/appfilter.xml")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(xml), encoding="utf-8")

    print(f"✅ appfilter.xml ({len(icons)} ícone(s))")
