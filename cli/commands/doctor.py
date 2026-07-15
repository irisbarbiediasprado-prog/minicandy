from cli.core.console import title, success, error, blank
from cli.doctor.checks import run as run_checks

NAME = "doctor"
HELP = "Verifica a saúde do projeto"

def line(label, ok, detail=""):
    icon = "✔" if ok else "✖"
    msg = f"{icon} {label}"
    if detail:
        msg += f" ({detail})"
    print(msg)

def run(args):
    title("MiniCandy Doctor")

    groups = [
        ("Projeto", 4),
        ("Android", 3),
        ("Banco", 1),
        ("Assets", 3),
        ("Ferramentas", 2),
        ("Git", 1),
    ]

    data = run_checks()
    i = 0
    failed = False

    for name, size in groups:
        print(name)
        print("──────────────")
        for _ in range(size):
            label, ok, detail = data[i]
            line(label, ok, detail)
            failed |= not ok
            i += 1
        blank()

    if failed:
        error("Projeto possui pendências.")
    else:
        success("Projeto pronto para desenvolvimento.")
