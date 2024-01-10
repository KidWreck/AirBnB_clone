#!/usr/bin/python3
'''
BaseModel module.
'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    BaseModel Class.
    '''

    def __init__(self, *args, **kwargs):
        '''
        INIT.
        '''
        my_time = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, my_time))
                else:
                    setattr(self, key, value)
        models.storage.new(self)

    def save(self):
        '''
        Update with the current datetime.
        '''
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        '''
        Returns a dictionary containing all keys/values of __dict__.
        '''
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        '''
        STR.
        '''
        my_class = self.__class__.__name__
        return "[{}] ({}) {}".format(my_class, self.id, self.__dict__)
