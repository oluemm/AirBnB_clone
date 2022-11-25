#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd



class HBNBCommand(cmd.Cmd):
    """The class that implements the console
    for the AirBnB clone web application
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program console
        """
        return True
    def do_EOF(self, args):
        """Ctrl + D to exit the console gracefully
        """
        return True
    def do_greet(self, args):
        print(f"Hi {args}")
    def emptyline(self):
        """Modify the empty line method to do nothing"""
        return

if __name__ == "__main__":
    HBNBCommand().cmdloop()
