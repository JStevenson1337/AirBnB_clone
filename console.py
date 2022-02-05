#!/usr/bin/env python3
import cmd
import os
import sys


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand that inherits from cmd.Cmd
    """
    prompt = '(hbnb) '
    counter = 0

    def do_quit(self, *args):
        """Type quit to quit the program"""
        return True

    def do_exit(self, *args):
        """Type exit to quit the program"""
        return True

    def do_EOF(self, *args):
        """Quit program with ctrl + D"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
