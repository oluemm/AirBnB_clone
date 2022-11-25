#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
import shlex
from models.base_model import BaseModel
from models import class_dict
from models import storage


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

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id.
        `Example:`
        >>> $ show BaseModel 1234-1234-1234.
        """
        args = shlex.split(args)
        # print(args)
        if len(args) == 0:  # check if no arg is passed
            print("** class name missing **")
            return
        elif args[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:  # check if id is missing
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            ciid = f"{class_name}.{instance_id}"
            all_instances = storage.all()
            if ciid in all_instances:
                show_ins = all_instances[ciid]
                # print(f"{class_name}[{instance_id}]")
                print(show_ins)
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file).
        `Example:`
        >>> $ destroy BaseModel 1234-1234-1234
        """
        args = shlex.split(args)
        # print(args)
        if len(args) == 0:  # check if no arg is passed
            print("** class name missing **")
            return
        elif args[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:  # check if id is missing
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            ciid = f"{class_name}.{instance_id}"
            all_instances = storage.all()
            if ciid in all_instances:
                del all_instances[ciid]
                storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
