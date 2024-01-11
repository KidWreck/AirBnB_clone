#!/usr/bin/python3
'''
Serializing and deserializing module.
'''
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    '''
    Storage class.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns the __objects dictionary.
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
         Sets <obj class name>.id.
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serializes into JSON and saves it.
        '''
        def_obj = FileStorage.__objects
        my_obj = {}

        for obj in def_obj.keys():
            my_obj[obj] = def_obj[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(my_obj, file)

    def reload(self):
        '''
        Deserializes from JSON.
        '''
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    my_obj = json.load(file)
                    for key, value in my_obj.items():
                        cls_name, obj_id = key.split(".")
                        any_cls = eval(cls_name)
                        acopy = any_cls(**args)
                        FileStorage.__objects[key] = acopy
                except Exception:
                    pass
