#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd



class HBNBCommand(cmd.Cmd):
    """The class that implements the console
    for the AirBnB clone web application
    """
    prompt = "(hbnb) "

    def quit(self):
        return True
    def EOF(self):
        return

if __name__ == "__main__":
    HBNBCommand().cmdloop()
