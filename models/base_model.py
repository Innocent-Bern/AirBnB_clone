#!/usr/bin/python3
""" base class module """

import uuid
from datetime import datetime


class BaseModel:
    """base class"""

    def __init__(self, *args, **kwargs):
        """initialize the model once it's created"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """returns class name, id and dictionary"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute 
        updated at with the current datetime
        """

        self.datetime = datetime.today()

    def to_dict(self):
        """
        returns a dictionary containing all key/values of __dict__
        """

        rtn_dict = self.__dict__.copy()
        rtn_dict["created_at"] = self.created_at.isoformat()
        rtn_dict["updated_at"] = self.updated_at.isoformat()
        rtn_dict["__class__"] = self.__class__.__name__

        return rtn_dict
