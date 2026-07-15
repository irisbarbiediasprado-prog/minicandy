from cli.core.console import title, step, success, blank

from cli.database.icons import rebuild

NAME = "scan"
HELP = "Atualiza o banco de dados"

def run(args):
    rebuild()
