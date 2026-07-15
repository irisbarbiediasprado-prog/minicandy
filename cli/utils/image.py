from pathlib import Path

def validate_png(path):
    path = Path(path)

    if not path.exists():
        return False, "Arquivo não encontrado."

    if path.suffix.lower() != ".png":
        return False, "O arquivo não é um PNG."

    return True, "OK"
