import re
import subprocess

from cli.core.console import step, success, error

def detect(query=None, activity=False):
    step("Consultando Package Manager")

    r = subprocess.run(
        ["cmd", "package", "list", "packages"],
        capture_output=True,
        text=True,
    )

    if r.returncode != 0:
        error("Falha ao consultar Package Manager.")
        return False

    packages = sorted(
        l.removeprefix("package:").strip()
        for l in r.stdout.splitlines()
        if l.strip()
    )

    if query:
        packages = [p for p in packages if query.lower() in p.lower()]

    success(f"{len(packages)} aplicativo(s) encontrado(s)")
    print()

    for pkg in packages:
        print(pkg)

        if not activity:
            continue

        p = subprocess.run(
            ["cmd", "package", "path", pkg],
            capture_output=True,
            text=True,
        )

        base = None
        for line in p.stdout.splitlines():
            if "base.apk" in line:
                base = line.removeprefix("package:")
                break

        if not base:
            continue

        a = subprocess.run(
            ["aapt2", "dump", "badging", base],
            capture_output=True,
            text=True,
        )

        m = re.search(r"launchable-activity: name='([^']+)'", a.stdout)

        if not m:
            print("  Activity: <não encontrada>")
            continue

        act = m.group(1)

        print(f"  Activity: {act}")
        print(f"  ComponentInfo{{{pkg}/{act}}}")

    return True
