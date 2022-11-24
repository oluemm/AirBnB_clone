#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd



class HBNBCommand(cmd.Cmd):
    """The class that implements the console
    for the AirBnB clone web application
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        return True
    def do_EOF(self, args):
        return
    def do_greet(self, args):
        print(f"Hi {args}")
if __name__ == "__main__":
    HBNBCommand().cmdloop()
