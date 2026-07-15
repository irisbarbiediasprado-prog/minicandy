from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def path(*parts):
    return ROOT.joinpath(*parts)

def exists(*parts):
    return path(*parts).exists()

def is_dir(*parts):
    return path(*parts).is_dir()
