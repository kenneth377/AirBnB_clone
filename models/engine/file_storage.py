import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        self.objects = value

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        # setattr(self.__objects, key, obj)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            newdict = {key: val.to_dict() for key ,val in self.objects.items()}
            json.dump(newdict,f)

    def reload(self):
        
        try:
            with open(self.__file_path, "r") as f:
                data = f.read()
                if not data:
                    self.__objects = {}
                else:
                    data = json.loads(data)
                    from models.base_model import BaseModel
                    for key, val in data.items():
                        self.__objects[key] = BaseModel(**val)

        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
        except Exception as e:
            print("An error occurred:", e)

        return self.__objects