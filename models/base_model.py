import uuid
import datetime
from models.__init__ import storage

class BaseModel:
    def __init__(self, *args, **kwargs) -> None:

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

        for key,val in kwargs.items():
            if not key == "__class__":
                if key == "created_at" or key == "updated_at":
                    val = datetime.datetime.strptime(val,"%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, val)
    
    def __str__(self) -> str:
        return f"[{self.__class__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        returndict = {}
        returndict["__class__"] = self.__class__.__name__
        for key,val in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                val = val.isoformat()
            returndict[key] = val

        return returndict

