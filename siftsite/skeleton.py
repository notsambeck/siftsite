#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
     fibonacci = siftsite.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import os
import logging
import requests

from siftsite import __version__

__author__ = "Sam Beck"
__copyright__ = "Sam Beck"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def upload_dir(filepath, label, source):
    '''upload whole directory (calls upload on all .png)'''
    base_dir = os.path.expanduser(os.path.dirname(filepath))
    files = os.listdir(base_dir)
    input('will upload {} files, continue or ctrl-c'.format(len(files)))
    for f in files:
        print(f[-4:])
        if f[-4:] == '.png':
            upload(os.path.join(base_dir, f), label, source)


def upload(filepath, label, source):
    '''POST request to your API with "files" key in requests data dict'''

    base_dir = os.path.expanduser(os.path.dirname(filepath))
    url = 'http://localhost:8000/api/'
    file_name = os.path.basename(filepath)
    with open(os.path.join(base_dir, file_name), 'rb') as fin:
        print('file:', base_dir, '/', file_name)
        POST_data = {'correct_label': label, 'source': source,
                     'filename': file_name}
        files = {'filename': (file_name, fin), 'file': file_name}
        resp = requests.post(url, data=POST_data, files=files)
        print(resp)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def parse_args(args):
    """Parse command line parameters
    Args:
      args ([str]): command line parameters as list of strings
    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version',
        version='siftsite {ver}'.format(ver=__version__))
    parser.add_argument(
        '--upload',
        dest="upload",
        help="Path to image file for upload to labler API",
        type=str)
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    return parser.parse_known_args(args)


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args, unknown = parse_args(args)
    if args.upload:
        upload(args.upload)
    else:
        print('yeah cool sure')


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
