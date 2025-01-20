import json


# Define the classes (assuming these are already defined in your code)
class FoodEntry:
    def __init__(self, food_type, quantity, feeding_time):
        self.food_type = food_type
        self.quantity = quantity
        self.feeding_time = feeding_time

    def to_dict(self):
        return {
            "food_type": self.food_type,
            "quantity": self.quantity,
            "feeding_time": self.feeding_time
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["food_type"], data["quantity"], data["feeding_time"])


class VetVisit:
    def __init__(self, visit_date, reason, outcome, vet_name):
        self.visit_date = visit_date
        self.reason = reason
        self.outcome = outcome
        self.vet_name = vet_name

    def to_dict(self):
        return {
            "visit_date": self.visit_date,
            "reason": self.reason,
            "outcome": self.outcome,
            "vet_name": self.vet_name
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["visit_date"], data["reason"], data["outcome"], data["vet_name"])


class ExerciseActivity:
    def __init__(self, type, duration, intensity_level):
        self.type = type
        self.duration = duration
        self.intensity_level = intensity_level

    def to_dict(self):
        return {
            "type": self.type,
            "duration": self.duration,
            "intensity_level": self.intensity_level
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["type"], data["duration"], data["intensity_level"])


class Tracker:
    def __init__(self):
        self.exercise_tracker_list = []
        self.vet_tracker_list = []
        self.food_tracker_list = []

    def to_dict(self):
        return {
            "exercise_tracker_list": [exercise.to_dict() for exercise in self.exercise_tracker_list],
            "vet_tracker_list": [vet_visit.to_dict() for vet_visit in self.vet_tracker_list],
            "food_tracker_list": [food_entry.to_dict() for food_entry in self.food_tracker_list]
        }

    @classmethod
    def from_dict(cls, data):
        tracker = cls()
        tracker.exercise_tracker_list = [ExerciseActivity.from_dict(item) for item in data["exercise_tracker_list"]]
        tracker.vet_tracker_list = [VetVisit.from_dict(item) for item in data["vet_tracker_list"]]
        tracker.food_tracker_list = [FoodEntry.from_dict(item) for item in data["food_tracker_list"]]
        return tracker


class Dog:
    def __init__(self, name, breed, gender):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.tracker = Tracker()

    def to_dict(self):
        return {
            "name": self.name,
            "breed": self.breed,
            "gender": self.gender,
            "tracker": self.tracker.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        dog = cls(data["name"], data["breed"], data["gender"])
        dog.tracker = Tracker.from_dict(data["tracker"])
        return dog


# Read JSON from file and populate dog_dict
def load_dog_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    dog_dict = {}
    for name, dog_data in data.items():
        dog_dict[name] = Dog.from_dict(dog_data)

    return dog_dict


# Example usage
file_path = 'dog_tracker_data.json'  # Path to your JSON file
dog_dict = load_dog_data_from_json(file_path)

# Verify the loaded data
for name, dog in dog_dict.items():
    print(f"Name: {dog.name}, Breed: {dog.breed}, Gender: {dog.gender}")
    print(f"Exercise Tracker: {dog.tracker.exercise_tracker_list}")
    print(f"Vet Tracker: {dog.tracker.vet_tracker_list}")
    print(f"Food Tracker: {dog.tracker.food_tracker_list}")
