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

    result = subprocess.run(
        ["./gradlew", "assembleDebug"],
        text=True
    )

    if result.returncode != 0:
        error("Falha no build.")
        return False

    apk = Path("app/build/outputs/apk/debug/app-debug.apk")

    if apk.exists():
        success(f"APK gerado: {apk}")
        return True

    error("APK não encontrado.")
    return False
