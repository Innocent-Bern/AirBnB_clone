#!/usr/bin/python3
""" base class module """

import models
import uuid
from datetime import datetime


class BaseModel:
    """base class"""

    def __init__(self, *args, **kwargs):
        """initialize the model once it's created"""

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """returns class name, id and dictionary"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated at with the current datetime
        """

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all key/values of __dict__
        """

        rtn_dict = self.__dict__.copy()
        rtn_dict["created_at"] = self.created_at.isoformat()
        rtn_dict["updated_at"] = self.updated_at.isoformat()
        rtn_dict["__class__"] = self.__class__.__name__

        return rtn_dict
