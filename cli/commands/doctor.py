from cli.core.console import title, step, success, blank

from pathlib import Path

NAME = "doctor"
HELP = "Verifica o ambiente"

def run(args):
    title("MiniCandy Doctor\n")

    checks = [
        ("app", Path("app").is_dir()),
        ("AndroidManifest.xml", Path("app/src/main/AndroidManifest.xml").exists()),
        ("assets", Path("assets").is_dir()),
        ("pixelart", Path("assets/pixelart").is_dir())
    ]

    ok = True

    for name, result in checks:
        print(("✔" if result else "✖"), name)
        ok &= result

    blank()

    if ok:
        print("Ambiente OK.")
    else:
        print("Existem problemas no projeto.")
