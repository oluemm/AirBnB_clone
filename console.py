#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import re
from shlex import split

import models

class HBNBCommand(cmd.Cmd):
    """the class that implment cmd for airBnB clone application"""

    prompt = "(hbnb)"
    storage = models.storage

    def empty(self):
        """commaned to exute an empty line + ENTER"""
        pass

    def EOF(self, arg):
        """ EOF signal to exit the program"""
        print("")
        return True
    def quit(self, argv):
        """when executed, exites the console"""
        return True
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
