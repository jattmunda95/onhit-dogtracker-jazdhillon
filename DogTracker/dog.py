"""
Dog Class

Author: Your Name
Date: January 19, 2025,
Description:
    This module defines the Dog class, representing a dog with attributes such as name, size, and gender.
    It also includes methods for managing dog profiles and tracking related information.

Methods:
    __init__(self, name, size, gender): Initializes a new Dog instance with the given name, size, and gender.
    dog_details(self): Prints the details of the dog instance.
    from_dict(cls, data): Class method to create a Dog instance from a dictionary.
    to_dict(self): Converts the Dog instance attributes to a dictionary.
    to_json(self): Converts the Dog instance attributes to JSON format.
"""

import json

import DogTracker.dog as dog_reference
from trackers.tracker import Tracker


class Dog:
    """
       A class used to represent a Dog and all associated classes

       :ivar str name: the name of the dog
       :ivar str size: the size of the dog [small, medium, large]
       :ivar str gender: the gender of the dog [male, female]
       :ivar Tracker tracker: the tracker associated with the dog, tracking various activities

       :param str name: The name of the dog
       :param str size: The size of the dog [small, medium, large]
       :param str gender: The gender of the dog [male, female]
   """

    def __init__(self, name: str, size: str, gender: str):
        """
        The initializer method for the Dog class, which takes the `name`, `size`, and `gender`
        and assigns them to the instance. Then the instance is saved to the `_all_dogs` list.

        :param str name: The name of the dog
        :param str size: The size of the dog [small, medium, large]
        :param str gender: The gender of the dog [male, female]
        """
        self.name = name
        self.size = size
        self.gender = gender
        self.tracker = Tracker()
        # self.date_of_birth = None

    def dog_details(self) -> None:
        """
        Function for retrieving details about the specific dog instance for printing and calling
        print_all_trackers method to print all trackers.
        :return: None
        """
        print(f"Dog Details")
        print(f"Name: {self.name}")
        print(f"Breed: {self.size}")
        print(f"Gender: {self.gender}")

        self.tracker.print_all_trackers(self.name)

    @classmethod
    def from_dict(cls, data: dict):
        """
        Class method to create a Dog instance from a dictionary.

        :param dict data: A dictionary containing dog attributes
        :return: A new Dog instance created from the dictionary data
        :rtype: dog_reference.Dog
        """
        dog = cls(data["name"], data["size"], data["gender"])
        dog.tracker = Tracker.from_dict(data["tracker"])
        return dog

    def to_dict(self) -> dict:
        """
        Converts class attributes to a dictionary.

        :return: A dictionary representation of the Dog instance attributes
        :rtype: dict
        """
        return {
            "name": self.name,
            "size": self.size,
            "gender": self.gender,
            "tracker": self.tracker.to_dict()
            # Add other attributes if needed
        }

    def to_json(self) -> str:
        """
        Converts class attributes to JSON format.

        :return: A JSON string representation of the Dog instance attributes
        :rtype: str
        """
        return json.dumps(self.to_dict(), indent=4)
