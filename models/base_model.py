#!/usr/bin/python3
""" A Base class that I will use for all the
other classes
"""
import uuid
import datetime
import models
import copy


class BaseModel:
    """Base methods and attributes for other classes"""
    def __init__(self, *args, **kwargs):
        """
        Base class constructor

        Args:
            args: inputs with no keys
            kwargs: key value inputs
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
        """Returns a string of the object
        """
        return "[{}] ({}) {}".format(
                self.___class__.__name__, self.id, selft.__dict__)

    def save(self):
        """Updates the updated_at
        with the current time
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict representation of all the keys/values of
        __dict__ of the instance.
        """
        newdict = copy.deepcopy(self.__dict__)
        newdict["__class__"] = self.__class__.__name__
        newdict['created_at'] = self.created_at.isoformat()
        newdict['updated_at'] = self.updated_at.isoformat()
        return (newdict)
