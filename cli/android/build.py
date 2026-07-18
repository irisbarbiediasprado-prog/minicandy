from pathlib import Path
import subprocess

from cli.core.console import title, step, success, error


def build():
    title("MiniCandy Build")

    gradlew = Path("./gradlew")
    if not gradlew.exists():
        error("gradlew não encontrado.")
        return False

    step("Compilando projeto")

    proc = subprocess.Popen(
        ["./gradlew", "assembleDebug"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    assert proc.stdout is not None

    for line in proc.stdout:
        if "No package ID 7f found for resource ID" in line:
            continue
        print(line, end="")

    proc.wait()

    if proc.returncode != 0:
        error("Falha no build.")
        return False

    apk = Path("app/build/outputs/apk/debug/app-debug.apk")

    if apk.exists():
        success(f"APK gerado: {apk}")
        return True

    error("APK não encontrado.")
    return False
