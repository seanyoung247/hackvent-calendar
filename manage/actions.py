"""
Implements modular server management commands
"""

import os


def commands():
    """ Enumerates all recognised commands """
    return {
        'addmodule': AddModule(),
        'remmodule': RemModule(),
        'help': ShowHelp(),
        '?': ShowHelp(),
    }


def get_command(command):
    """ Returns the command object that implements the requested command """
    commandList = commands()
    command = commandList.get(command)
    if command:
        return command
    
    return commandList.get('help')


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
        return 'Usage: python3 manage.py addmodule <module name>'

    def __call__(self, args):
        """ Generates a new server module and files in the required format """
        if not self.valid_args(args, 2):
            return
        module_name = args[1]
        try:
            os.mkdir(module_name)
            # Create files...
        except OSError as e:
            print(e)


class RemModule(Command):
    """ Removes an existing server module """
    @staticmethod
    def help():
        return 'Usage: python3 manage.py remmodule <module name>'

    def __call__(self, args):
        """ Removes an existing server module and files """
        if not self.valid_args(args, 2):
            return
        print("I'm not implimented yet, sorry")


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
