from pathlib import Path

def mkdir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def write(path, text):
    Path(path).write_text(text, encoding="utf-8")
