#!/usr/bin/python3
""" The base_model module
"""
import uuid
import datetime
import copy
import models


class BaseModel:
    """class BaseModel that defines all common attr/method
    """
    def __init__(self, *args, **kwargs):
        """
        Class constructor

        Args:
            args: non-keyworded argument list
            kwargs: keyworded argument list with key and values
        """
        if kwargs:
            for keys, value in kwargs.items():
                if keys == '__class__':
                    continue
                elif keys == "created_at" or keys == "updated_at":
                    formatt = '%Y-%m-%dT%H:%M:%S.%f'
                    value = datetime.datetime.strptime(value, formatt)
                setattr(self, keys, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Convert object into a human readable string
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_att
        witth the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """
        newdict = copy.deepcopy(self.__dict__)
        newdict["__class__"] = self.__class__.__name__
        newdict['created_at'] = self.created_at.isoformat()
        newdict['updated_at'] = self.updated_at.isoformat()
        return (newdict)
