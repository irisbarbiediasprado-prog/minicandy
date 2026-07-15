from importlib import import_module
from pathlib import Path

COMMANDS = {}

for file in sorted(Path(__file__).parent.glob("*.py")):
    if file.stem.startswith("_") or file.stem == "__init__":
        continue

    module = import_module(f"{__name__}.{file.stem}")

    if hasattr(module, "NAME"):
        COMMANDS[module.NAME] = module
