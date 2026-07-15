from importlib import import_module
from pathlib import Path

def load():
    commands = {}

    commands_dir = Path(__file__).resolve().parents[1] / "commands"

    for file in sorted(commands_dir.glob("*.py")):
        if file.stem.startswith("_"):
            continue

        module = import_module(f"cli.commands.{file.stem}")

        if hasattr(module, "NAME"):
            commands[module.NAME] = module

    return commands
