#!/usr/bin/python3
""" class module"""

import json


class FileStorage:
    """filestorage class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        o_dict = {obj: self.__objects[obj].to_dict()
                  for obj in self.__objects.keys()}
        with open(self.__fiile_path, "w") as f:
            json.dump(o_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(self.__file_path) as f:
                o_dict = json.load(f)
                for obj in o_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
