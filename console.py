#!/usr/bin/env python3
import cmd
import os
import sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
           'City': City, 'Amenity': Amenity, 'Place': Place,
           'Review': Review}


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand that inherits from cmd.Cmd
    """
    prompt = '(hbnb) '

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

    def do_create(self, args):
        """
        Type 'create' and a class name to create a new instance
        of that class
        """
        if not args:
            print('** class name missing **')
        elif args in classes.keys():
            new_inst = classes[args]()
            FileStorage.save(new_inst)
            print(new_inst.id)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
