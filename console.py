import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import datetime

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
            print(storage.objects[key])
        
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
        
        except KeyError:
            print("** no instance found **")
            return
        

    def do_all(self,arg):
        returnarray =[]
        if not arg:
            for key,entry in storage.objects.items():
                returnarray.append(str(entry))
            print(returnarray)
            return

            
        params = arg.split(" ")


        if len(params)==1:
            try:
                globals()[params[0]]
                for key, entry in storage.objects.items():
                    if isinstance(entry,globals()[params[0]]):
                        returnarray.append(str(entry))
                print(returnarray)
                return

            except KeyError:
                print(f"** class doesn't exist **")
                return
            
    def do_update(self,arg):
        # args = arg.split(" ")
        if not arg:
            print("** class name missing **")
            return
        
        params =arg.split(" ")
        try:
            globals()[params[0]]
        
        except KeyError:
            print("** class doesn't exist **")
            return
        
        if len(params) < 2:
            print("** instance id missing **")
            return
        key = f"{params[0]}.{params[1]}"
        
        data =storage.objects[key]
        if key not in storage.objects.keys():
            print("no instance found")
            return
        
        if len(params) < 3:
            print("** attribute name missing **")
            return
        
        attribute = params[2]
        if attribute not in data.to_dict().keys():
            print("** attribute doesn't exist **")
            return
        
        if len(params) < 4:
            print("**value missing**")
            return
        
        value = params[3]

        try:
            # typ2 = type(getattr(data,attribute))
            # print(typ2(value))
            # if isinstance(getattr(data,attribute), datetime.datetime):
            #     setattr(data,attribute, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
            # setattr(data,attribute, value)
            # print(data)
            
            if isinstance(data, str):
                setattr(data,attribute, str(value))
            elif isinstance(data, int):
                setattr(data,attribute, int(value))
            elif isinstance(data, float):
                setattr(data,attribute, float(value))
            else:
                print("** attribute type not supported **")
            return
           

        except Exception as e:
            print(f"An error occured: {e}")

    def do_save(self,arg):
        storage.save() 

    def do_stringi(self,arg):
        print(storage.objects)



if __name__ == '__main__':
    HBNBCommand().cmdloop()