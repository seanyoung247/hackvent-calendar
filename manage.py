
import os
import sys


class add_module:
    def help(self):
        return "Usage: "

    def __call__(self, args):
        """ Generates a new server module and files in the required format """
        if (len(args) < 2):
            print(self.help())
            return
        
        print(args)


def commands():
    return {
        "addmodule": add_module(),
        "help": show_help,
        "?": show_help,
    }


def show_help(args = None):
    print('I heard you need help!')


def decode_args(args):
    return commands().get(args[0])


def main(args):
    command = decode_args(args)
    if command:
        command.help()
        command(args)
    else:
        print('Command line argument not recognised!')


if __name__ == '__main__':
    if len(sys.argv) > 1: 
        main(sys.argv[1:])
    else: 
        # Print help here...
        pass
