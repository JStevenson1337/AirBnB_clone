#!/usr/bin/python3
""" Test console.py """

import unittest
import console
from console import HBNBCommand

class test_console(unittest.TestCase):
    """ Test console.py """

    def test_console(self):
        """ Test console.py """
        self.assertEqual(console.HBNBCommand().onecmd("create"), None)
        self.assertEqual(console.HBNBCommand().onecmd("show"), None)
        self.assertEqual(console.HBNBCommand().onecmd("all"), None)
        self.assertEqual(console.HBNBCommand().onecmd("update"), None)
        self.assertEqual(console.HBNBCommand().onecmd("destroy"), None)
        self.assertEqual(console.HBNBCommand().onecmd("help"), None)
        self.assertEqual(console.HBNBCommand().onecmd("quit"), None)
        self.assertEqual(console.HBNBCommand().onecmd("EOF"), None)

    def test_console_create(self):
        """ Test console.py """
        self.assertEqual(console.HBNBCommand().onecmd("create"), None)
        self.assertEqual(console.HBNBCommand().onecmd("create User"), None)
        self.assertEqual(console.HBNBCommand().onecmd("create User name"), None)
        self.assertEqual(console.HBNBCommand().onecmd("create User name age"), None)

    def test_console_show(self):
        """ Test console.py """
        self.assertEqual(console.HBNBCommand().onecmd("show"), None)
        self.assertEqual(console.HBNBCommand().onecmd("show User"), None)
        self.assertEqual(console.HBNBCommand().onecmd("show User name"), None)
        self.assertEqual(console.HBNBCommand().onecmd("show User name age"), None)
        self.assertEqual(console.HBNBCommand().onecmd("show User name age id"), None)

    def test_console_all(self):
        """ Test console.py """
        self.assertEqual(console.HBNBCommand().onecmd("all"), None)
        self.assertEqual(console.HBNBCommand().onecmd("all User"), None)
        self.assertEqual(console.HBNBCommand().onecmd("all User name"), None)
        self.assertEqual(console.HBNBCommand().onecmd("all User name age"), None)
        self.assertEqual(console.HBNBCommand().onecmd("all User name age id"), None)


