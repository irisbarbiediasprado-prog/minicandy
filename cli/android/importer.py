import re
import subprocess
from pathlib import Path
import json

from PIL import Image

from cli.database.icons import load, save


def run(query):
    src = Path(query)

    if not src.exists():
        d = Path("/storage/emulated/0/Download")

        for ext in ("png", "jpg", "jpeg", "webp", "avif"):
            f = d / f"{query}.{ext}"
            if f.exists():
                src = f
                break
        else:
            print(f"❌ Imagem {query} não encontrada em {d}")
            return

    query = src.stem.lower()

    aliases_file = Path("assets/database/aliases.json")
    aliases = json.loads(aliases_file.read_text(encoding="utf-8")) if aliases_file.exists() else {}
    alias = aliases.get(query)

    dst = Path(f"assets/pixelart/originals/{query}.png")
    dst.parent.mkdir(parents=True, exist_ok=True)

    Image.open(src).convert("RGBA").save(dst)

    result = subprocess.run(
        ["cmd", "package", "list", "packages"],
        capture_output=True,
        text=True,
        check=False,
    )

    if alias:
        packages = [alias]
    else:
        packages = [
            p.removeprefix("package:").strip()
            for p in result.stdout.splitlines()
            if query in p.lower()
        ]

    if not packages:
        raise RuntimeError("Aplicativo não encontrado.")

    if len(packages) > 1:
        print("🔎 Múltiplos aplicativos encontrados:")
        for i, pkg in enumerate(packages, 1):
            print(f"{i}) {pkg}")

        choice = input(f"Escolha [1-{len(packages)}]: ")

        try:
            pkg = packages[int(choice) - 1]
        except Exception:
            print("❌ Escolha inválida.")
            return
    else:
        pkg = packages[0]

    result = subprocess.run(
        [
            "cmd",
            "package",
            "resolve-activity",
            "--user",
            "0",
            "-a",
            "android.intent.action.MAIN",
            "-c",
            "android.intent.category.LAUNCHER",
            pkg,
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    match = re.search(r"name=([^\n]+)", result.stdout)

    if not match:
        raise RuntimeError("Launcher Activity não encontrada.")

    activity = match.group(1).strip()
    component = f"ComponentInfo{{{pkg}/{activity}}}"

    db = load()

    for icon in db["icons"]:
        if icon["name"] == query or icon["drawable"] == query:
            icon["package"] = pkg
            icon["activity"] = activity
            icon["component"] = component
            save(db)

            print("✅ Atualizado")
            print(f"Package..... {pkg}")
            print(f"Activity.... {activity}")
            print(f"Component... {component}")
            return

    db["icons"].append(
        {
            "name": query,
            "drawable": query,
            "file": f"assets/pixelart/originals/{query}.png",
            "package": pkg,
            "activity": activity,
            "component": component,
        }
    )

    save(db)

    print("✅ Novo ícone importado")
    print(f"Package..... {pkg}")
    print(f"Activity.... {activity}")
    print(f"Component... {component}")
