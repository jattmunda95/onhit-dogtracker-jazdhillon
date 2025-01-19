"""
Dog Class

Author: Your Name
Date: January 19, 2025,
Description:
    This module defines the Dog class, representing a dog with attributes such as name, breed, and age.
    It also includes methods for managing dog profiles and tracking related information.

Methods:
    __init__(self, name, breed, age): Initializes a new Dog instance with the given name, breed, and age.
    get_all_dogs(cls): Class method to retrieve all dog instances.
    save_to_csv(cls, file_name): Class method to save all dog instances to a CSV file.
    update_name(self, new_name): Updates the dog's name.
    update_breed(self, new_breed): Updates the dog's breed.
    update_age(self, new_age): Updates the dog's age.
"""

import csv
import datetime

class Dog:

    def __init__(self, name: str, breed: str, gender: str, date_of_birth_str: str):
        """
        The initializer method for Dog class, which takes the `name`, `breed`, `gender` and `date_of_birth`
        and assigns them to instance. Then the instance is saved to the `_all_dogs` list.
        :param name: name of the dog
        :param breed: breed name of the dog
        :param gender: gender of the dog (M/F)
        :param date_of_birth: date of birth of the dog as a string, which is taken and then converted to a datetime object
        """
        self._name = name
        self._breed = breed
        self._gender = gender
        self._date_of_birth = None
        with open('all_dogs.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Breed", "Gender", "Date of Birth"])
            writer.writerow([self._name, self._breed, self._gender, self._date_of_birth])

    def __validate_date_of_birth(self, date_of_birth_str: str) -> datetime.datetime:
        empty_date_string = str()
        try:
            datetime.datetime.strptime(date_of_birth_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date of birth")
            return False
        return datetime.datetime.strptime(date_of_birth_str, "%Y-%m-%d")
