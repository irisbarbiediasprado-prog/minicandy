from pathlib import Path

NAME = "generate"
HELP = "Gera arquivos do icon pack"

def generate_drawable(icons):
    xml = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<resources>'
    ]

    for icon in icons:
        xml.append(f'    <item drawable="{icon.stem}" />')

    xml.append("</resources>")

    out = Path("app/src/main/res/xml/drawable.xml")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(xml), encoding="utf-8")

    print(f"✅ drawable.xml ({len(icons)} ícone(s))")

def generate_appfilter(icons):
    xml = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<resources>'
    ]

    for icon in icons:
        xml.append(f'    <!-- TODO: ComponentInfo para {icon.stem} -->')
        xml.append(f'    <item component="ComponentInfo{{}}" drawable="{icon.stem}" />')
        xml.append("")

    xml.append("</resources>")

    out = Path("app/src/main/res/xml/appfilter.xml")
    out.write_text("\n".join(xml), encoding="utf-8")

    print(f"✅ appfilter.xml ({len(icons)} ícone(s))")

def run(args):
    if not getattr(args, "_unknown", None):
        print("Uso:")
        print("  mc generate drawable")
        print("  mc generate appfilter")
        return

    icons = sorted(Path("assets/pixelart/originals").glob("*.png"))

    match args._unknown[0]:
        case "drawable":
            generate_drawable(icons)
        case "appfilter":
            generate_appfilter(icons)
        case _:
            print("Alvo desconhecido.")
