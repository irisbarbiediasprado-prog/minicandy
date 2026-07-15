import argparse
from cli.commands.doctor import run

parser = argparse.ArgumentParser(prog="mc")
sub = parser.add_subparsers(dest="command")

sub.add_parser("doctor", help="Verifica o ambiente")

args = parser.parse_args()

if args.command == "doctor":
    run()
else:
    parser.print_help()
