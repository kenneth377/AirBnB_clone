import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self,arg):
        return True
    
    def do_EOF(self,arg):
        print()
        return True
    
    def do_create(self,arg):
        if not arg:
            print("** class name missing **")
            return
        
        funcs = arg.split(" ")[0]

        try:
            cls = globals()[funcs]
            cls()
            

        except KeyError:
            print(f"** class doesn't exist **")
            return

    def do_show(self,arg):

        if not arg:
            print("** class name missing **")
            return
        
        params = arg.split(" ")
        
        if len(params)<2:
            print("** instance id missing **")
            return

        try:
            globals()[params[0]]

        except KeyError:
            print(f"** class doesn't exist **")
            return

        key = f"{params[0]}.{params[1]}"
        try:
            print(f"{storage.objects[key]}")
        
        except KeyError:
            print("** no instance found **")
            return

    
    def do_destroy(self,arg):
        if not arg:
            print("** class name missing **")
            return
        
        params = arg.split(" ")
        
        if len(params)<2:
            print("** instance id missing **")
            return

        try:
            globals()[params[0]]

        except KeyError:
            print(f"** class doesn't exist **")
            return

        key = f"{params[0]}.{params[1]}"

        try:
            storage.objects.pop(key)
            storage.save()
        
        except KeyError:
            print("** no instance found **")
            return
        
    def do_stringi(self,arg):
        print(storage.objects)



if __name__ == '__main__':
    HBNBCommand().cmdloop()