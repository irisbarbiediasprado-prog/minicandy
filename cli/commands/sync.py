from argparse import Namespace

from cli.commands import scan
from cli.commands import stats
from cli.generators import drawable
from cli.generators import appfilter

NAME = "sync"
HELP = "Sincroniza o projeto"

def run(args):
    print("🍬 MiniCandy Sync")
    print()

    print("▶ Scan")
    scan.run(Namespace())

    print()
    print("▶ Generate drawable")
    drawable.generate()

    print()
    print("▶ Generate appfilter")
    appfilter.generate()

    print()
    print("▶ Stats")
    stats.run(Namespace())
