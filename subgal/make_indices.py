#!/usr/bin/env python3

import sys

DEFAULT_BASE_URL = "http://localhost:8080/"

__doc__ = """Usage: subgal make-indices [options] <correlations.json>
       subgal make-indices --help

Options:
-c, --clobber                    Allow overwriting of existing files
-h, --help                       This help
-v, --version                    Print version and exit
-i, --index-root=<path>          Where the index_....html files will be created
                                 [DEFAULT: .]
-b, --base-url=<url>             All images and indices will have <url> at the beginning
                                 [DEFAULT: {1}]
""".format(sys.argv[0], DEFAULT_BASE_URL)


from docopt import docopt


def vprint(given_verbosity, verbosity, string):
  if given_verbosity <= verbosity:
    print(string)


def main(argv):
  args = docopt(__doc__, argv=argv)

  print(args)

if __name__ == "__main__":
  main(sys.argv)
