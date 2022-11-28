#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models import class_dict
from models import storage

def parse(arg):
    """Parse the command line arguments"""
    # search for strings that contain curly_braces
    curly_braces = re.search(r"\{(.*?)\}", arg)
    # search for strings that contain brackets
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:  # no curly_braces
        if brackets is None:  # no brackets
            # simply split the string
            return [i.strip(",") for i in split(arg)]
        else:  # if brackets
            # slice the str of args at the index whr
            # the brackets starts.
            start_idx = brackets.span()[0]
            lexer = split(arg[:start_idx])
            # remove all commas from each items
            retl = [i.strip(",") for i in lexer]
            # append the arguments in brackets
            retl.append(brackets.group())
            return retl
    else:  # if curly_braces
            # slice the str of args at the index whr
            # the curly_braces starts
        start_idx = curly_braces.span()[0]
        lexer = split(arg[:start_idx])
        # remove all commas from each items
        retl = [i.strip(",") for i in lexer]
        # append the arguments in curly_braces
        retl.append(curly_braces.group())
        return retl


def check_args(args):
    """Checks if args is valid
    Args:
        args (str): the string containing the arguments passed to a command
    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
        return
    elif arg_list[0] not in class_dict.keys():
        print("** class doesn't exist **")
        return
    else:
        return arg_list

class HBNBCommand(cmd.Cmd):
    """
    The class that implements the console
    for the AirBnB clone web application
    """
    prompt = "(hbnb) "
    class_lists = [i for i in class_dict.keys()]

    def do_quit(self, args):
        """
        Quit command to exit the program console
        """
        return True

    def do_EOF(self, args):
        """
        Ctrl + D to exit the console gracefully
        """
        print()
        return True

    def emptyline(self):
        """
        Modify the empty line method to do nothing
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of a given Model,
        saves it (to the JSON file) and prints the id.
        `Example:`$ create BaseModel
        `Example:`$ <class_name>.create()
        """
        args = check_args(args)
        if not args:
            return
        # evaluate the class_arg & create a new instance
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id.
        `Example:`
        >>> $ show BaseModel 1234-1234-1234.
        >>> $ <class_name>.show(1234-1234-1234)
        """
        args = check_args(args)
        if not args:
            return
        if len(args) < 2:  # check if id is missing
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]  # 2nd argument is instance_id
            # ciid stands for class instance id
            # gotten from concatenation of class_name and instance
            ciid = f"{class_name}.{instance_id}"
            # get all available instances saved
            all_instances = storage.all()
            if ciid in all_instances:  # if ciid exists
                # save instance to a temporary variable show_ins
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
        >>> $ <class_name>.destroy(1234-1234-1234)
        """
        args = check_args(args)
        if not args:
            return
        if len(args) < 2:  # check if id is missing
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            ciid = f"{class_name}.{instance_id}"
            all_instances = storage.all()
            if ciid in all_instances:
                # delete the key and its value
                del all_instances[ciid]
                # save the instances object
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name.
        `Example:`
        >>> $ all
        >>> $ all BaseModel
        >>> $ <class_name>.all()
        """
        args = split(args)
        all_instances = storage.all()
        my_list = []
        if len(args) == 0:  # check if no arg is passed
            my_list= [
                str(all_instances[instances])
                for instances in all_instances.keys()
                ]
                # my_list.append(str(all_instances[instances]))
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

        >>> update <class name> <id> <attribute name> '<attribute value>'

        >>> $ <class_name>.update(<id> <attribute name> '<attribute value>')

        >>> <class name>.update(<id>, <dictionary representation>)
        """
        args = check_args(args)
        my_instances = storage.all()
        if not args:
            return
        class_name = args[0]
        # try:
        #     if class_name not in class_dict.keys():
        #         print("** class doesn't exist **")
        # except Exception:
        #     print("** class name missing **")
        #     return
        try:
            id = args[1]
            ciid = f"{class_name}.{id}"
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

        if ciid not in my_instances.keys():
            print("** no instance found **")
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
        """
        Modify the default to catch varying commands

        #### Example usage
        * (hbnh) User.all()
        * (hbnh) User.show("5f3f49e0-7499-4ef1-9558-5412e05c9333")
        * (hbnh) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
        * (hbnh) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88",
        "age", 89)
        * (hbnh) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88",
        {'first_name': "John", "age": 89})
        """
        dict_funcs = {
            "all()": self.do_all,
            "count()": self.do_count,
            "show()": self.do_show,
            "destroy()": self.do_destroy,
            "update()": self.do_update,
            "create()": self.do_create
        }
        lst = line.replace(")", "").replace("(", "() ")\
            .replace(".", " ").replace(",", " ")\
                .replace(":", " ").replace("{", " ")\
                    .replace("}", " ").replace("  ", " ")
        lst = split(lst)
        # print(lst, "\n")
        cls_name = lst[0]
        try:
            method = lst[1]
        except IndexError:
            print(f"*** Unknown syntax: {line}")
            return

        if method in dict_funcs:
            method = lst[1]
            if len(lst) == 2:
                dict_funcs[method](cls_name)
            elif len(lst) == 3:
                arguments = f"'{cls_name}' '{lst[2]}'"
                # print(f"{method}({arguments})")
                dict_funcs[method](arguments)
            elif len(lst) >= 4 and len(lst[3:]) % 2 == 0:
                lst_to_dct = lst[3:]
                # print(lst_to_dct)
                # using dict comprehension to get k & v pairs
                try:
                    dic = {
                        lst_to_dct[i]: lst_to_dct[i + 1]
                        for i in range(0, len(lst_to_dct), 2)
                        }
                    # print(dic)
                except IndexError:
                    print("** value missing **")
                    return
                for k, v in dic.items():
                    arguments = f"{cls_name} {lst[2]} {k} {v}"
                    dict_funcs[method](arguments)
            else:
                rem = " ".join(str(i) for i in lst[2:])
                # print(rem)
                arguments = f"'{cls_name}' {rem}"
                # '{lst[3]}' '{lst[4]}'"
                dict_funcs[method](arguments)
        else:
            print(f"*** Unknown syntax: {line}")

    def do_count(self, args: str):
        """
        #### Returns:
        Total number of instances a class has
        #### Usage:
        <class_name>.count()
        count <class_name>
        `Example`:
        * BaseModel.count()
        * count User
        """
        args = check_args(args)
        if not args:
            return
        all_instances = storage.all()
        my_list = []
        class_name = args[0]
        for instances in all_instances.keys():
            if str(instances).startswith(class_name):
                my_list.append(str(all_instances[instances]))
        print(len(my_list))
# ===================================================================
# ====================== Auto Completions Functions =================
# ===================================================================

    def complete_all(self, text, line, begidx, endidx):
        if not text:
            completions = self.class_lists[:]
        else:
            completions = [
                f
                for f in self.class_lists
                if f.startswith(text)
                ]
        return completions

    def complete_count(self, text, line, begidx, endidx):
        if not text:
            completions = self.class_lists[:]
        else:
            completions = [
                f
                for f in self.class_lists
                if f.startswith(text)
                ]
        return completions

    def complete_create(self, text, line, begidx, endidx):
        if not text:
            completions = self.class_lists[:]
        else:
            completions = [
                f
                for f in self.class_lists
                if f.startswith(text)
                ]
        return completions

    def complete_show(self, text, line, begidx, endidx):
        if not text:
            # print(line)
            completions = self.class_lists[:]
        else:
            # print(line)
            completions = [
                f
                for f in self.class_lists
                if f.startswith(text)
                ]
        return completions


if __name__ == "__main__":
    HBNBCommand().cmdloop()
