"""
Implements modular server management commands
"""

import os


class Commands():
    commandList = {}

    @classmethod
    def registerCommand(cls, command):
        cls.update(command.name(), command)



def commands():
    """ Enumerates all recognised commands """
    return {
        'addmodule': AddModule(),
        'remmodule': RemModule(),
        'help': ShowHelp(),
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
    def __init_subclass__(cls, **kwargs):
        """ Automatically registers commands in the command list """
        super().__init_subclass__(**kwargs)
        # Register here ...

    @staticmethod
    def name():
        raise NotImplementedError()

    @staticmethod
    def help():
        """ returns a string of help text for using this command """
        raise NotImplementedError()

    @classmethod
    def valid_args(cls, args, count):
        """ Checks that the correct number of arguments has been provided """
        if len(args) >= count:
            return True
        print(cls.help())
        return False

    def __call__(self, args):
        pass


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
        print('Usage: python3 manage.py <command> <options>')
        print('Commands:')
        commandlist = commands()
        for (key,value) in commandlist.items():
            print(f"{key:>15} : {value.help()}")
