from cli.database.icons import rebuild

NAME = "scan"
HELP = "Atualiza o banco de dados"

def run(args):
    rebuild()
