import json
import os
import re
import sys

from trackers.exercise.objects.exercise_activity import ExerciseActivity
from trackers.food.objects.food_entry import FoodEntry
from trackers.vet.objects.vet_visits import VetVisit

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Tracker:
    """
    A class used to represent the Tracker, which tracks various activities for a dog.

    Attributes
    ----------
    exercise_tracker_list : list
        A list to store exercise activities.
    vet_tracker_list : list
        A list to store vet visit records.
    food_tracker_list : list
        A list to store food entries.

    Methods
    -------
    __init__()
        Initializes a new Tracker instance.
    add_to_exercise_tracker()
        Adds a new exercise activity to the exercise tracker list.
    add_to_vet_tracker()
        Adds a new vet visit to the vet tracker list.
    add_to_food_list()
        Adds a new food entry to the food tracker list.
    print_all_trackers(dogname)
        Prints all tracker logs for a given dog.
    from_dict(cls, data)
        Class method to create a Tracker instance from a dictionary.
    to_dict()
        Converts the Tracker instance attributes to a dictionary.
    to_json()
        Converts the Tracker instance attributes to JSON format.
    """

    def __init__(self):
        """
        Initializes a new Tracker instance.

        This constructor sets up the following attributes as empty lists:

        :ivar exercise_tracker_list: A list to store exercise-related data.
        :type exercise_tracker_list: list
        :ivar vet_tracker_list: A list to store veterinary-related data.
        :type vet_tracker_list: list
        :ivar food_tracker_list: A list to store food tracking information.
        :type food_tracker_list: list
        """
        self.exercise_tracker_list = []
        self.vet_tracker_list = []
        self.food_tracker_list = []

    def print_all_trackers(self, dog_name: str):
        """
        Prints all tracker logs for a given dog.

        This method displays the exercise, vet, and food tracker logs associated
        with the specified dog's name. Each tracker list is printed with a header,
        and a message is shown if a tracker is empty.

        :param dog_name: The name of the dog for which to print the tracker logs.
        :type dog_name: str

        :returns: None
        """

        print(f"######### Tracker Log for : {dog_name} #########")

        print("Exercise Tracker List:")
        if self.exercise_tracker_list:
            for exercise in self.exercise_tracker_list:
                print(exercise)
        else:
            print("No exercise records.")

        print("\nVet Tracker List:")
        if self.vet_tracker_list:
            for vet_visit in self.vet_tracker_list:
                print(vet_visit)
        else:
            print("No vet visit records.")

        print("\nFood Tracker List:")
        if self.food_tracker_list:
            for food_entry in self.food_tracker_list:
                print(food_entry)
        else:
            print("No food records.")

    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates a Tracker instance from a dictionary.

        This method initializes a new `Tracker` instance by populating its
        attributes from the provided dictionary. Each tracker list is
        reconstructed using corresponding `from_dict` methods for their
        respective objects.

        :param data: A dictionary containing tracker attributes with the keys:
                     - "exercise_tracker_list": A list of dictionaries representing exercise activities.
                     - "vet_tracker_list": A list of dictionaries representing vet visits.
                     - "food_tracker_list": A list of dictionaries representing food entries.
        :type data: dict

        :returns: A new Tracker instance populated with data from the dictionary.
        :rtype: Tracker
        """
        tracker = cls()
        tracker.exercise_tracker_list = [ExerciseActivity.from_dict(item) for item in data["exercise_tracker_list"]]
        tracker.vet_tracker_list = [VetVisit.from_dict(item) for item in data["vet_tracker_list"]]
        tracker.food_tracker_list = [FoodEntry.from_dict(item) for item in data["food_tracker_list"]]
        return tracker

    def to_dict(self) -> dict:
        """
        Converts the Tracker instance attributes to a dictionary.

        This method creates a dictionary representation of the `Tracker` instance,
        where all attributes are transformed into JSON-serializable structure.

        :returns: A dictionary representation of the `Tracker` instance with keys:
                  - "exercise_tracker_list": A list of dictionaries representing exercise activities.
                  - "vet_tracker_list": A list of dictionaries representing vet visits.
                  - "food_tracker_list": A list of dictionaries representing food entries.
        :rtype: dict
        """
        return {
            "exercise_tracker_list": [exercise.to_dict() for exercise in self.exercise_tracker_list],
            "vet_tracker_list": [vet_visit.to_dict() for vet_visit in self.vet_tracker_list],
            "food_tracker_list": [food_entry.to_dict() for food_entry in self.food_tracker_list]
        }

    def to_json(self) -> str:
        """
        Converts the Tracker instance attributes to a JSON string.

        This method serializes the `Tracker` instance into a JSON-formatted string
        by first converting it to a dictionary using the `to_dict` method and then
        using `json.dumps`.

        :returns: A JSON string representation of the `Tracker` instance attributes.
        :rtype: str
        """
        return json.dumps(self.to_dict(), indent=4)
