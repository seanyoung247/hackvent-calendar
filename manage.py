
""" Simplifies basic management operations of the modular flask server """

import sys
from manage.actions import get_command


def main(args):
    """ Entry point """
    if len(args) <= 1:
        get_command('help')()
        return

    args = args[1:]
    command = get_command(args[0])
    command(args)


if __name__ == '__main__':
    main(sys.argv)
