#!/usr/bin/python3
""" base class module """


import datetime


class BaseModel():
    """base class"""

    id = str(uuid.uuid4())

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        pass

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        pass
