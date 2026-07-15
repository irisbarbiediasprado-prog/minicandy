from pathlib import Path

NAME = "generate"
HELP = "Gera arquivos do icon pack"

def generate_drawable(_):
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


def generate_appfilter(_):
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


def register(subparsers):
    parser = subparsers.add_parser(NAME, help=HELP)
    actions = parser.add_subparsers(dest="generate_command", required=True)

    drawable = actions.add_parser("drawable", help="Gera drawable.xml")
    drawable.set_defaults(func=generate_drawable)

    appfilter = actions.add_parser("appfilter", help="Gera appfilter.xml")
    appfilter.set_defaults(func=generate_appfilter)
