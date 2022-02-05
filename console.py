#!/usr/bin/env python3
import cmd
import os


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand that inherits from cmd.Cmd
    """
    prompt = '(hbnb) '
    counter = 0

    def execute_quit(self, args):
        """Quit command to exit the program"""
        return True

    def execute_EOF(self, args):
        """Quit command to exit the program at the end of the file"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()


