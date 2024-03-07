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
                    
                    
                    for key, val in data.items():
                        try:
                            if val["__class__"] == "BaseModel":
                                from models.base_model import BaseModel
                                self.__objects[key] = BaseModel(**val)

                            elif val["__class__"] == "User":
                                from models.user import User
                                self.__objects[key] = User(**val)

                            elif val["__class__"] == "Amenity":
                                from models.amenity import Amenity
                                self.__objects[key] = Amenity(**val)
                            
                            elif val["__class__"] == "Place":
                                from models.place import Place
                                self.__objects[key] = Place(**val)

                            elif val["__class__"] == "City":
                                from models.city import City
                                self.__objects[key] = City(**val)

                            elif val["__class__"] == "Review":
                                from models.review import Review
                                self.__objects[key] = Review(**val)

                            else:
                                from models.state import State
                                self.__objects[key] = State(**val)
                        
                        except Exception as e:
                            print("An error occurred:", e)
                            return


        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
        except Exception as e:
            print("An error occurred:", e)
            return

        return self.__objects