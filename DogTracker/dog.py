"""
Dog Class

Author: Your Name
Date: January 19, 2025
Description:
    This module defines the Dog class, representing a dog with attributes such as name, breed, and gender.
    It also includes methods for managing dog profiles and tracking related information.

Methods:
    __init__(self, name, breed, gender): Initializes a new Dog instance with the given name, breed, and gender.
    get_all_dogs(cls): Class method to retrieve all dog instances.
    save_to_csv(cls, file_name): Class method to save all dog instances to a CSV file.
    update_name(self, new_name): Updates the dog's name.
    update_breed(self, new_breed): Updates the dog's breed.
    update_age(self, new_age): Updates the dog's age.
"""
import json
from trackers.tracker import Tracker

class Dog:
    def __init__(self, name, breed, gender):
        """
        The initializer method for the Dog class, which takes the `name`, `breed`, and `gender`
        and assigns them to the instance. Then the instance is saved to the `_all_dogs` list.

        :param name: Name of the dog
        :param breed: Breed name of the dog
        :param gender: Gender of the dog (M/F)
        """
        self.name = name
        self.breed = breed
        self.gender = gender
        self.tracker = Tracker()
        # self.date_of_birth = None

    def dog_details(self):
        print(f"Dog Details")
        print(f"Name: {self.name}")
        print(f"Breed : {self.breed}")
        print(f"Gender: {self.gender}")

        self.tracker.print_all_trackers(self.name)

    def to_dict(self):
        """Convert class attributes to a dictionary."""
        return {
            "name": self.name,
            "breed": self.breed,
            "gender": self.gender,
            "tracker": self.tracker.to_dict()
            # Add other attributes if needed
        }
    def to_json(self):
        """Convert class attributes to JSON."""
        return json.dumps(self.to_dict(), indent=4)
