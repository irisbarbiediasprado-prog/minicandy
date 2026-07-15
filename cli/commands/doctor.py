import shutil
from pathlib import Path
from cli.core.console import title, section, check

NAME = "doctor"
HELP = "Verifica o ambiente"

ROOT = Path(__file__).resolve().parents[2]

def run(args=None):
    title("MiniCandy Doctor")

    section("Ferramentas")
    check("Git", shutil.which("git") is not None)
    check("Python", shutil.which("python3") is not None)

    section("\nProjeto")
    check("app/", (ROOT / "app").is_dir())
    check("build.gradle.kts", (ROOT / "build.gradle.kts").exists())
    check("AndroidManifest.xml", (ROOT / "app/src/main/AndroidManifest.xml").exists())

    section("\nStatus")
    print("Environment OK")
