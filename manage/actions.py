"""
Implements modular server management commands
"""

import os


class Commands():
    commandList = {}

    @classmethod
    def register_command(cls, command):
        cls.commandList.update(command.name(), command)
    
    @classmethod
    def list(cls):
        return cls.commandList

    @classmethod
    def get_command(cls, command):
        return cls.commandList.get(command)


class Command:
    """ Base class for management commands """
    def __init_subclass__(cls, **kwargs):
        """ Automatically registers commands in the command list """
        super().__init_subclass__(**kwargs)
        Commands.register_command(cls)

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
    def name():
        return "addmodule"

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
    def name():
        return "remmodule"

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
    def name():
        return "help"

    @staticmethod
    def help():
        return 'Shows help text'

    def __call__(self, args=None):
        print('Usage: python3 manage.py <command> <options>')
        print('Commands:')
        commandlist = Commands.list()
        for (key,value) in commandlist.items():
            print(f"{key:>15} : {value.help()}")
