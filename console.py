#!/usr/bin/python3
'''
The console.
'''
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    '''
    Console class.
    '''
    prompt = "(hbnb) "
    my_valid = ["BaseModel", "User", "Amenity",
                "Place", "Review", "State", "City"]

    def emptyline(self):
        '''
        Do nothing when empty line.
        '''
        pass

    def do_EOF(self, arg):
        '''
        (Ctrl+D) to exit the program.
        '''
        return True

    def do_quit(self, arg):
        '''
        Quit command to exit the program.
        '''
        return True

    def do_create(self, arg):
        '''
        Creates a new instance of BaseModel, saves it and prints the id.
        '''
        cmd = shlex.split(arg)
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.my_valid:
            print("** class doesn't exist **")
        else:
            new = eval(f"{cmd[0]}()")
            storage.save()
            print(new.id)

    def do_show(self, arg):
        '''
        Show an instance based on the class name and id.
        '''
        cmd = shlex.split(arg)
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.my_valid:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            my_obj = storage.all()
            key = "{}.{}".format(cmd[0], cmd[1])
            if key in my_obj:
                print(my_obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id.
        '''
        cmd = shlex.split(arg)
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.my_valid:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            my_obj = storage.all()
            key = "{}.{}".format(cmd[0], cmd[1])
            if key in my_obj:
                del my_obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        '''
        List all instances based or not on the class name.
        '''
        cmd = shlex.split(arg)
        my_obj = storage.all()
        if len(cmd) == 0:
            for key, value in my_obj.items():
                print(str(value))
        elif cmd[0] not in self.my_valid:
            print("** class doesn't exist **")
        else:
            for key, value in my_obj.items():
                if key.split('.')[0] == cmd[0]:
                    print(str(value))

    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id.
        '''
        cmd = shlex.split(arg)
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.my_valid:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            my_obj = storage.all()
            key = "{}.{}".format(cmd[0], cmd[1])
            if key not in my_obj:
                print("** no instance found **")
            elif len(cmd) < 3:
                print("** attribute name missing **")
            elif len(cmd) < 4:
                print("** value missing **")
            else:
                upd = my_obj[key]
                att_name = cmd[2]
                att_value = cmd[3]
                try:
                    att_value = eval(att_value)
                except Exception:
                    pass
                setattr(upd, att_name, att_value)
                upd.save


if __name__ == '__main__':
    HBNBCommand().cmdloop()
