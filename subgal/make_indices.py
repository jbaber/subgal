#!/usr/bin/env python3

import sys
import os
import json
import collections

DEFAULT_BASE_URL = "http://localhost:8080/"

__doc__ = """Usage: subgal make-indices [options] [-v ...] <correlations.json>
       subgal make-indices --help

Options:
-h, --help                       This help
-i, --index-root=<path>          Where the index_....html files will be created
                                 [DEFAULT: .]
-v, --verbosity                  Number of v's is level of verbosity
                                 (No -v results in silence, -vvvv is
                                 super verbose)
-b, --base-url=<url>             All images and indices will have <url> at the beginning
                                 [DEFAULT: {1}]
""".format(sys.argv[0], DEFAULT_BASE_URL)


from docopt import docopt


def vprint(given_verbosity, verbosity, string):
  if given_verbosity <= verbosity:
    print(string)


def directories_to_original_filenames(correlation):
  to_return = collections.defaultdict(list)
  for original_filename in correlation.keys():
    directory = os.path.dirname(original_filename)
    to_return[directory].append(original_filename)
  return to_return


def main(argv):
  args = docopt(__doc__, argv=argv)

  base_url = args['--base-url']
  index_root = args['--index-root']
  json_filename = args['<correlations.json>']
  verbosity = args['--verbosity']
  v = verbosity

  with open(json_filename) as f:
    correlations = json.load(f)

  dtoof = directories_to_original_filenames(correlations)
  print(dtoof)

  for directory in dtoof.keys():
    index_filename = "index_" + directory.replace(os.path.sep, "__") + ".html"
    vprint(1, v, f"Creating {index_filename}")


if __name__ == "__main__":
  main(sys.argv)
