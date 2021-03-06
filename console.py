#!/usr/bin/env python3
""" Console for the application. """
import cmd

import models
from models import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class that contains the console for the application.
    """

    prompt = '(hbnb) '
    __classes = {'BaseModel': BaseModel, 'User': User,
                 'State': State, 'City': City, 'Amenity': Amenity,
                 'Place': Place, 'Review': Review}

    def do_create(self, *args):
        """
        Creates an instance of a class
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(args[0] + "." + str(eval(args[0] + "()")))

    def do_update(self, *args):
        """
        Updates an instance based on the class name and id
        """
        if len(args) == 0:
            print("** class name missing **")
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
                if args[2] in ['created_at', 'updated_at']:
                    print("** attribute name cannot be 'created_at' or "
                          "'updated_at' **")
                else:
                    FileStorage.all()[key].__dict__[args[2]] = args[3]
                    FileStorage.all()[key].save()
            else:
                print("** no instance found **")

    def do_all(self, *args):
        """ Prints all instances """
        if args[0] == '':
            print(models.storage.all())
        elif args and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in models.storage.all().items()
                   if args[0] in k])

    def do_count(self, *args):
        """ Counts the number of instances of a class """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(len([v for k, v in FileStorage.all().items()
                       if args[0] in k]))

    def do_show(self, *args):
        """ Prints an instance """
        if len(args) == 0:
            print("** class name missing **")
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
        """ Deletes an instance """
        if len(args) == 0:
            print("** class name missing **")
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
        Default method for the console.
        """
        print("*** Unknown syntax: {}".format(line))

    def do_quit(self, *args):
        """ Quits the application"""
        return True

    def do_exit(self, *args):
        """ Quits the application"""
        return True

    def do_EOF(self, *args):
        """ Quits the application with an end of file"""
        return True

    def emptyline(self):
        """ empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
