
""" Simplifies basic management operations of the modular flask server """

# import os
import sys


class Command:
    """ Base class for management commands """
    @staticmethod
    def help():
        """ returns a string of help text for using this command """
        return None

    @classmethod
    def valid_args(cls, args, count):
        """ Checks that the correct number of arguments has been provided """
        if len(args) >= count:
            return True
        print(cls.help())
        return False

    def __call__(self, args):
        """ Ensures the correct number of arguments are passed """


class AddModule(Command):
    """ Adds a new server module """
    @staticmethod
    def help():
        return 'Usage: python manage.py addmodule <module name>'

    def __call__(self, args):
        """ Generates a new server module and files in the required format """
        if not self.valid_args(args, 2):
            return
        # add module code here
        print(args)


class ShowHelp(Command):
    """ Shows all commands help text """
    @staticmethod
    def help():
        return 'Shows help text'

    def __call__(self, args=None):
        print('Usage: python manage.py <command> <options>')
        print('Commands:')
        commandlist = commands()
        for (key,value) in commandlist.items():
            print(f"{key:>15} : {value.help()}")



def commands():
    """ Enumerates all recognised commands """
    return {
        'addmodule': AddModule(),
        'help': ShowHelp(),
        '?': ShowHelp(),
    }


def decode_args(args):
    """ Returns which command object implements the requested command """
    command = commands().get(args[0])
    if command:
        return command
    return commands().get('help')


def main(args):
    """ Entry point """
    if len(args) <= 1:
        commands().get('help')()
        return

    args = args[1:]
    command = decode_args(args)
    command(args)


if __name__ == '__main__':
    main(sys.argv)
