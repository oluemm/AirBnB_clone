#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models import class_dict
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The class that implements the console
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
        """
        Creates a new instance of a given Model,
        saves it (to the JSON file) and prints the id.
        `Example:`$ create BaseModel
        """
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
        """
        Prints the string representation of an instance
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
        """
        Deletes an instance based on the class name
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

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name.
        `Example:`
        >>> $ destroy BaseModel 1234-1234-1234
        """
        args = shlex.split(args)
        all_instances = storage.all()
        my_list = []
        if len(args) == 0:  # check if no arg is passed
            for instances in all_instances:
                my_list.append(str(all_instances[instances]))
            print(my_list)
        elif args[0] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            for instances in all_instances.keys():
                if str(instances).startswith(class_name):
                    my_list.append(str(all_instances[instances]))
            print(my_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the
        JSON file).
        `Example:`
        >>> $ update BaseModel 1234-1234-1234 email "aibnb@mail. com".
        Usage: update <class name> <id> <attribute name> '<attribute value>'
        """
        from models import FileStorage
        args = shlex.split(args)
        my_instances = storage.all()
        try:
            class_name = args[0]
            if class_name not in class_dict.keys():
                print("** class doesn't exist **")
        except Exception:
            print("** class name missing **")
            return
        try:
            id = args[1]
            ciid = f"{class_name}.{id}"
            if ciid not in my_instances.keys():
                print("** no instance found **")
                return
        except Exception:
            print("** instance id missing **")
            return
        try:
            attribute_name = args[2]
        except Exception:
            print("** attribute name missing **")
            return
        try:
            attribute_val = args[3]
        except Exception:
            print("** value missing **")
            return

        update_dict = {}  # initialize empty dict
        #  loop thru loaded instance's key & value pairs
        for k, v in my_instances.items():
            # add them to update_dict
            # but bcos values are Model instances,
            # we have to call our to_dict() method to
            # serialize them
            update_dict[k] = v.to_dict()
        # now that we have a nested dictionary
        # we get the id of the instance to be updated,
        # and assign it to the variable update_me
        update_me = update_dict[ciid]
        # now we can edit the dict with the user's k:v in args
        update_me[attribute_name] = attribute_val
        for k in update_dict.keys():
            # get the class name of each instance
            cls_name = update_dict[k]["__class__"]
            # get an instance, and update it if identified by user
            new_instance = update_dict[k]
            storage.new(eval(cls_name)(**new_instance))
            storage.save()

    def default(self, line: str):
        """Modify the default to catch varying commands
        `Example usage`
        * User.all()
        """
        parser_dict = {
            "all": self.do_all,
            "count": self.do_count
        }
        lst = []
        for args in line.split('.'):
            lst.append(args)
        lst[1] = lst[1].replace("()", "")
        cls_name = lst[0]
        method = lst[1]
        if method in parser_dict:
            parser_dict[method](cls_name)

    def do_count(self, args: str):
        args = shlex.split(args)
        all_instances = storage.all()
        my_list = []
        if args[0] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            for instances in all_instances.keys():
                if str(instances).startswith(class_name):
                    my_list.append(str(all_instances[instances]))
            print(len(my_list))



if __name__ == "__main__":
    HBNBCommand().cmdloop()
