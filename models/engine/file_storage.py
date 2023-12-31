#!/usr/bin/python3
""" Defines FileStorage """
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Declares FileStorage class
    """
    __file_path = "file.json"
    __objects = dict()
    className = {'BaseModel': BaseModel,
                 'User': User,
                 'City': City,
                 'State': State,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review}

    def all(self):
        """ Returns the entire dictionary """
        return self.__objects

    def new(self, obj):
        """ Sets a new object in __objects
            Args:
                obj: Represents the new obj to add to the dict
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        s_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(s_objs))

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                s_objs = json.load(file)
                for key, value in s_objs.items():
                    # self.__objects[key] = base_model.BaseModel(**value)
                    self.__objects[key] = FileStorage\
                                        .className[key.split('.')[0]](**value)
