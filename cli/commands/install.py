from pathlib import Path
import shutil
import subprocess

NAME = "install"
HELP = "Copia o APK para Download e abre o Material Files"

APK = Path("app/build/outputs/apk/debug/app-debug.apk")
DEST = Path("/storage/emulated/0/Download/minicandy.apk")

def register(subparsers):
    p = subparsers.add_parser(NAME, help=HELP)
    p.set_defaults(func=run)

def run(args):
    if not APK.exists():
        print("❌ APK não encontrado. Execute: ./mc build")
        return

    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(APK, DEST)

    print(f"✅ APK copiado para {DEST}")

    subprocess.run([
        "am", "start",
        "-n",
        "me.zhanghai.android.files/me.zhanghai.android.files.filelist.FileListActivity",
        "-d",
        "file:///storage/emulated/0/Download"
    ])

    print()
    print("👉 O Material Files foi aberto.")
    print("👉 Toque em minicandy.apk para instalar.")
