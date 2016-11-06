#!/usr/bin/env python
"""
__author__ = 
__date-created__ = 10/19/16
"""

import argparse

VERSION = '0.1.0'
LAST_MOD = '10/19/16'

# Customize
program_desc = 'v{}, last-modified {}: \n \
Single sentence describing module purpose.'.format(VERSION, LAST_MOD)


class StatsDB:

    def __init__(self):
        pass


# May or may not need a parser, but just in case... 
def get_parser():
    """
    generic parser uses above info
    """
    parser = argparse.ArgumentParser(description=program_desc)

    # Customize
    parser.add_argument('-o1', '--option1', dest='[option1_arg]', action='store',
                        help="does what option1 is supposed to do")

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    # Customize (refactor opt1 -> blah)
    if args.opt1:
        # Customize
        what_option_one_does = args.opt1
        print('\nOption Selected: {}'.format(what_option_one_does))


if __name__ == '__main__':
    main()
