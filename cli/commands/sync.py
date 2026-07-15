from cli.core.console import title, step, success, blank

from argparse import Namespace

from cli.commands import scan
from cli.commands import stats
from cli.generators import drawable
from cli.generators import appfilter

NAME = "sync"
HELP = "Sincroniza o projeto"

def run(args):
    title("MiniCandy Sync")
    blank()

    step("Scan")
    scan.run(Namespace())

    blank()
    step("Generate drawable")
    drawable.generate()

    blank()
    step("Generate appfilter")
    appfilter.generate()

    blank()
    step("Stats")
    stats.run(Namespace())
