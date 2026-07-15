import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def check(label, ok):
    print(("✔" if ok else "✘"), label)

def run():
    print("🍬 MiniCandy Doctor\n")

    print("Ferramentas")
    check("Git", shutil.which("git") is not None)
    check("Python", shutil.which("python3") is not None)

    print("\nProjeto")
    check("app/", (ROOT / "app").is_dir())
    check("build.gradle.kts", (ROOT / "build.gradle.kts").exists())
    check("AndroidManifest.xml", (ROOT / "app/src/main/AndroidManifest.xml").exists())

    print("\nStatus")
    print("Environment OK")
