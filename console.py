#!/usr/bin/env python3
import cmd
from models import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine import file_storage
import models
import os
classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
           'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand that inherits from cmd.Cmd
    """
    prompt = '(hbnb) '

    def do_create(self, args):
        """
        Creates an instance of a class
        """
        if len(args) < 1:
            print('** class name missing **')
        elif args in classes.keys():
            new_inst = classes[args]()
            new_inst.save()
            print(new_inst.id)
        else:
            print("** class doesn't exist **")

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
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if len(args) == 0:
            print(FileStorage.all())
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print([v for k, v in FileStorage.all().items()
                   if args[0] in k])

    def do_count(self, *args):
        """
        Counts the number of instances of a class
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(len([v for k, v in FileStorage.all().items()
                       if args[0] in k]))

    def do_show(self, *args):
        """ Prints string representation of an instance """
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
        """
        Deletes an instance based on the class name and id
        """
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
