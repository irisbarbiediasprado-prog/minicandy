from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

APP_DIR = PROJECT_ROOT / "app"
CLI_DIR = PROJECT_ROOT / "cli"
DOCS_DIR = PROJECT_ROOT / "docs"

DEBUG = False
