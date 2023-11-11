#!/usr/bin/python3
'''Define class HBNBCommand'''
import cmd
from models import BaseModel, storage, User


class HBNBCommand(cmd.Cmd):
    '''class HBNBCommand'''

    prompt = "(hbnb) "
    class_list = ["BaseModel", "User"]

    def complete_create(self, text, line, begidx, endidx):
        """Custom tab completion for the 'create' command's argument"""
        return [name for name in self.class_list if name.startswith(text)]

    def do_create(self, line):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id'''
        if len(line.split()) > 1:
            return
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                b = BaseModel()
                b.save()
                print(b.id)
            elif line == "User":
                u = User()
                u.save()
                print(u.id)

    @staticmethod
    def make_dict():
        '''
        Return a dictionary with the key: id and value: object
        '''
        dic = {}
        all_objs = storage.all()
        for obj in all_objs.values():
            dic[obj.to_dict()["id"]] = obj
        return dic

    def do_show(self, line):
        '''Prints the string representation of an instance based on the class
        name and id'''
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
            elif args[1] and len(args) == 2:
                dic = self.make_dict()
                if args[1] not in dic:
                    print("** no instance found **")
                else:
                    print(dic[args[1]])

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
            elif args[1] and len(args) == 2:
                dic = self.make_dict()
                if args[1] not in dic:
                    print("** no instance found **")
                else:
                    dic = storage.all()
                    if args[0] == "BaseModel":
                        del dic["BaseModel." + args[1]]
                    elif args[0] == "User":
                        del dic["User." + args[1]]
                    storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances based or not
        on the class name'''
        if arg and arg not in self.class_list:
            print("** class doesn't exist **")
        elif not arg or arg in self.class_list:
            dic = self.make_dict()
            list_obj = []
            for obj in dic.values():
                list_obj.append(str(obj))
            print(list_obj)

    def do_update(self, line):
        '''Updates an instance based on the class name and id by adding or
        updating attribute'''
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
            elif args[1] and len(args) >= 2:
                dic = self.make_dict()
                if args[1] not in dic:
                    print("** no instance found **")
                else:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(args) == 3:
                            print("** value missing **")
                        else:
                            obj = dic[args[1]]
                            if args[3][0] == '"':
                                values = args[3].split('"')
                            else:
                                return
                            setattr(obj, args[2], values[1])
                            storage.save()

    def emptyline(self):
        pass

    def do_EOF(self, line):
        '''EOF command to exit the program\n'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
