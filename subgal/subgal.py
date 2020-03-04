#!/usr/bin/env python3

import sys
from docopt import docopt
import subprocess


__doc__ = """Usage: subgal <command> [<args>...]
       subgal help

Options:

Commands:
  make-thumbs
  make-indices
  update

See 'subgal <command> --help' for more information on a specific command."""


def main():
  args = docopt(__doc__, version='1.0.0', options_first=True)
  argv = [args['<command>']] + args['<args>']

  if args['<command>'] in ('help', None):
    print(__doc__)
    exit(0)

  if args['<command>'] == "make-thumbs":
    from subgal import make_thumbs
    exit(make_thumbs.main(argv))


if __name__ == "__main__":
  main()