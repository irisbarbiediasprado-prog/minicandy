from pathlib import Path
import json
import subprocess
import sys

def check(label, ok, detail=""):
    return (label, ok, detail)

def run():
    results = []

    # Projeto
    results.append(check("app/", Path("app").is_dir()))
    results.append(check("assets/", Path("assets").is_dir()))
    results.append(check("cli/", Path("cli").is_dir()))
    results.append(check("docs/", Path("docs").is_dir()))

    # Android
    results.append(check(
        "AndroidManifest.xml",
        Path("app/src/main/AndroidManifest.xml").exists()
    ))
    results.append(check(
        "drawable.xml",
        Path("app/src/main/res/xml/drawable.xml").exists()
    ))
    results.append(check(
        "appfilter.xml",
        Path("app/src/main/res/xml/appfilter.xml").exists()
    ))

    # Banco
    db = Path("assets/database/icons.json")
    count = 0

    if db.exists():
        try:
            count = len(json.loads(db.read_text(encoding="utf-8"))["icons"])
        except Exception:
            pass

    results.append(check("icons.json", db.exists(), f"{count} ícone(s)"))

    # Assets
    for folder in (
        "assets/pixelart/originals",
        "assets/pixelart/exported",
        "assets/pixelart/preview",
    ):
        results.append(check(folder, Path(folder).is_dir()))

    # Ferramentas
    results.append(check(
        "Python",
        True,
        sys.version.split()[0]
    ))

    results.append(check(
        "Gradle Wrapper",
        Path("gradlew").exists()
    ))

    # Git
    git = Path(".git").exists()
    branch = ""

    if git:
        try:
            branch = subprocess.check_output(
                ["git", "branch", "--show-current"],
                text=True
            ).strip()
        except Exception:
            branch = "?"

    results.append(check("Git", git, branch))

    return results
