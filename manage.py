import os
import sys


def show_help():
    print('I heard you need help!')

def ensure_args(count):
    def decorator(func):

        def wrapper(*args, **kwargs):
            if len(*args) >= count:
                func(*args, **kwargs)
            else:
                print('ARRRGH! not enough args!')

        return wrapper
    return decorator


@ensure_args(count = 2)
def add_module(args):
    """ Generates a new server module and files in the required format """

    print(f"Creating module: {args[1]}")
    # More here...


def decode_args(args):
    commands = {
        "addmodule": add_module,
        "help": show_help,
        "?": show_help,
    }
    return commands.get(args[0])


def main(args):
    command = decode_args(args)
    if command:
        command(args)
    else:
        print('Command line argument not recognised!')
        

if __name__ == '__main__':
    main(sys.argv[1:])
