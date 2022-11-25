#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
import shlex
import models


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
        print()
        return True

    def do_greet(self, args):
        print(f"Hi {args}")

    def emptyline(self):
        """Modify the empty line method to do nothing"""
        pass

    def do_create(self, args):
        '''
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id.
            `Example:`$ create BaseModel
        '''
        if len(args) == 0:  # check if no arg is passed
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            # evaluate the class_arg & create a new instance
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

        except Exception:    # if class doesn't exist
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
