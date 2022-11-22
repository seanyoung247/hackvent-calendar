
""" Simplifies basic management operations of the modular flask server """

import sys
from server.actions import Commands


def main(args):
    """ Entry point """
    if len(args) <= 1:
        Commands.get_command('help')()
        return

    args = args[1:]
    command = Commands.get_command(args[0])
    command(args)


if __name__ == '__main__':
    main(sys.argv)
