from cli.metadata import NAME, VERSION, AUTHOR, DESCRIPTION

NAME = "version"
HELP = "Mostra informações da CLI"

def run(args=None):
    print(f"{NAME} {VERSION}")
    print(DESCRIPTION)
    print(f"Author: {AUTHOR}")
