import argparse
from cli.commands.doctor import run as doctor

def main():
    parser = argparse.ArgumentParser(prog="mc")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("doctor", help="Verifica o ambiente")

    args = parser.parse_args()

    if args.command == "doctor":
        doctor()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
