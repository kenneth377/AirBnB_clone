import cmd
import json
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
import re


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
        
        if len(params)<2 or not params[1]:
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
            
    def do_update(self,arg,**kwargs):
        # args = arg.split(" ")
        if kwargs:
           ckey = f'{kwargs["classname"]}.{kwargs["key"]}'
           data = storage.objects[ckey]
           for key,val in kwargs.items():
            print(key)
            if not key == "classname" and not key == "key":
                setattr(data,key,val)
            
            print(data)
            return

        if not arg:
            print("** class name missing **")
            return
        
        params =arg.split(" ")
        try:
            globals()[params[0]]
        
        except KeyError:
            print("** class doesn't exist **")
            return
        
        if not params[1]:
            print("** instance id missing **")
            return
        key = f"{params[0]}.{params[1]}"
        
        if key not in storage.objects.keys():
            print("no instance found")
            return
        
        if len(params) < 3:
            print("** attribute name missing **")
            return
        
        data =storage.objects[key]
        
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
            # print(attribute)
            # print(value)
            
            if isinstance(getattr(data, attribute), int):
                value = int(value)
            elif isinstance(getattr(data, attribute), float):
                value = float(value)
            elif isinstance(getattr(data, attribute), str):
                value = str(value)
            else:
                print("** attribute type not supported **")
                return

            setattr(data, attribute, value)
            print(data)

           

        except Exception as e:
            print(f"An error occured: {e}")

    def do_save(self,arg):
        storage.save()

    def default(self, arg):
        try:
            parts = arg.split('.')
            if len(parts) == 2:
                method_name, funcnnargs = parts
                funcname,funcargs = funcnnargs.split("(")
                if funcname == "all":
                    self.do_all(method_name)
                elif funcname == "count":
                    count= 0
                    for item in storage.objects.values():
                        st = str(item).split("]")[0]
                        mainst= st.lstrip("[")
                        if mainst == method_name:
                            count+=1
                    print(count)
                elif funcname == "show":
                    argi =funcargs.rstrip(")")
                    arg = f"{method_name} {argi}"
                    print(argi)
                    self.do_show(arg)

                elif funcname == "destroy":
                    argi =funcargs.rstrip(")")
                    arg = f"{method_name} {argi}"
                    
                    self.do_destroy(arg)

                elif funcname == "update":
                    argi =funcargs.rstrip(")")
                    if "{" in argi:
                        keyargs = argi.split(",",1)
                        keyid = keyargs[0].lstrip('"').rstrip('"')
                        realkey = keyargs[1].replace("'","\"")
                        keydict = json.loads(realkey.lstrip().rstrip())
                        keydict["key"] = keyid
                        keydict["classname"] = method_name
                        argk = ""
                        self.do_update(argk,**keydict)
                    else:
                        keyargs = argi.split(",")
                        keyid = keyargs[0].lstrip('"').rstrip('"')
                        
                        keyattribute = keyargs[1].lstrip(' "').rstrip('"')
                        keyvalue = keyargs[2].lstrip(' "').rstrip('"')
                        arg = f"{method_name} {keyid} {keyattribute} {keyvalue}"
                        self.do_update(arg)
                    
            else:
                print("Invalid input format. Use 'ClassName.method'.")

        except Exception as e:
            print("Error:", e)


    def do_stringi(self,arg):
        print(storage.objects)



if __name__ == '__main__':
    HBNBCommand().cmdloop()