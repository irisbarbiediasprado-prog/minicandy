import re
import subprocess
from cli.database.icons import load, save

def run(query):
    r = subprocess.run(
        ["cmd","package","list","packages"],
        capture_output=True,
        text=True,
        check=False,
    )

    packages = [
        p.removeprefix("package:").strip()
        for p in r.stdout.splitlines()
        if query.lower() in p.lower()
    ]

    if not packages:
        print("❌ Aplicativo não encontrado.")
        return

    pkg = packages[0]

    base = None
    r = subprocess.run(
        ["cmd","package","path",pkg],
        capture_output=True,
        text=True,
        check=False,
    )

    for line in r.stdout.splitlines():
        if "base.apk" in line:
            base = line.removeprefix("package:")
            break

    if not base:
        print("❌ base.apk não encontrada.")
        return

    r = subprocess.run(
        ["aapt2","dump","badging",base],
        capture_output=True,
        text=True,
        check=False,
    )

    m = re.search(r"launchable-activity: name='([^']+)'", r.stdout)

    if not m:
        print("❌ Launcher Activity não encontrada.")
        return

    activity = m.group(1)
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

    print("❌ Ícone não encontrado no banco.")
