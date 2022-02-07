#!/usr/bin/env python3
import cmd
from models import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand that inherits from cmd.Cmd
    """
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_create(self, *args):
        """
        Creates an instance of a class
        """
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = args[0]()
            print(new_obj.id)
            FileStorage.save()

    def do_update(self, *args):
        """
        Updates an instance based on the class name and id
        """
        if not args:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        elif len(args) < 3:
            print('** attribute name missing **')
        elif len(args) < 4:
            print('** value missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in FileStorage.all().keys():
                FileStorage.all()[key].__dict__[args[2]] = args[3]
                FileStorage.save()
            else:
                print("** no instance found **")

    def do_all(self, *args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if not args:
            print(FileStorage.all())
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print([v for k, v in FileStorage.all().items() if
                   args[0] in k])

    def do_show(self, *args):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        if not args:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in FileStorage.all().keys():
                print(FileStorage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, *args):
        """
        Deletes an instance based on the class name and id
        """
        if not args:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in FileStorage.all().keys():
                del FileStorage.all()[key]
                FileStorage.save()
            else:
                print("** no instance found **")

    def default(self, line):
        """
        Default method that prints an error message
        if the command is not recognized
        """
        print("*** Unknown syntax: {}".format(line))

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
    # HBNBCommand().onecmd("create BaseModel")
