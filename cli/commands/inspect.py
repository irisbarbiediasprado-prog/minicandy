from pathlib import Path
import json
import subprocess
from PIL import Image

NAME = "inspect"
HELP = "Inspeciona um ícone"

def register(sub):
    p = sub.add_parser(NAME, help=HELP)
    p.add_argument("name")
    p.set_defaults(func=run)

def ok(v):
    return "✔" if v else "✖"

def section(t):
    print(f"\n{t}")
    print("──────────────")

def run(args):
    name = args.name
    png = Path(f"assets/pixelart/originals/{name}.png")
    db = Path("assets/database/icons.json")
    drawable = Path("app/src/main/res/xml/drawable.xml")
    appfilter = Path("app/src/main/res/xml/appfilter.xml")

    print("🍬 MiniCandy Inspect")
    section("Nome")
    print(name)

    section("Arquivo")
    print(f"{ok(png.exists())} {png}")
    if png.exists():
        img = Image.open(png)
        print(f"✔ {img.width}×{img.height}")
        print(f"✔ {img.mode}")
        print(f"✔ {png.stat().st_size//1024} KB")

    icon = None
    if db.exists():
        data = json.loads(db.read_text(encoding="utf-8"))
        icon = next((i for i in data["icons"] if i.get("name")==name), None)

    section("Banco")
    print(f"{ok(icon)} Registro encontrado")
    if icon:
        print(f"{ok(icon.get('drawable'))} Drawable........ {icon.get('drawable','<ausente>')}")
        print(f"{ok(icon.get('file'))} File............ {icon.get('file','<ausente>')}")
        print(f"{ok(icon.get('package'))} Package......... {icon.get('package','<ausente>')}")
        print(f"{ok(icon.get('activity'))} Activity........ {icon.get('activity','<ausente>')}")
        print(f"{ok(icon.get('component'))} Component....... {icon.get('component','<ausente>')}")

    section("Drawable.xml")
    txt = drawable.read_text(encoding="utf-8") if drawable.exists() else ""
    hit = f'drawable="{name}"' in txt
    print(f"{ok(hit)} Encontrado")
    if hit:
        for l in txt.splitlines():
            if f'drawable="{name}"' in l:
                print(l.strip())
                break

    section("AppFilter.xml")
    txt = appfilter.read_text(encoding="utf-8") if appfilter.exists() else ""
    hit = f'drawable="{name}"' in txt
    print(f"{ok(hit)} Encontrado")
    if hit:
        for l in txt.splitlines():
            if f'drawable="{name}"' in l:
                print(l.strip())
                break

    section("Sistema")
    pkg = icon.get("package") if icon else None
    if pkg:
        r = subprocess.run(["cmd","package","resolve-activity",pkg],capture_output=True,text=True)
        print(f"{ok(r.returncode==0)} Package instalado")
        if r.stdout:
            print(r.stdout.strip())
    else:
        print("✖ Package não pode ser verificado")
        print("(motivo: package ausente)")

    section("Diagnóstico")
    if not icon:
        print("O ícone não existe no banco.")
        print("\nPróxima ação")
        print("──────────────")
        print(f"./mc icon import {name}")
    elif not all(icon.get(k) for k in ("package","activity","component")):
        print("O PNG foi importado, porém o banco está incompleto.")
        print("O ícone nunca será aplicado porque não existe package/activity associados.")
        print("\nPróxima ação")
        print("──────────────")
        print(f"./mc icon import {name}")
    elif not hit:
        print("O banco está correto, mas o appfilter.xml não foi gerado.")
        print("\nPróxima ação")
        print("──────────────")
        print("./mc generate")
    else:
        print("✔ Cadeia completa.")
