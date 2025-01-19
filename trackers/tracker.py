import json
from trackers.vet.objects.vet_visits import VetVisit
from trackers.exercise.objects.exercise_activity import ExerciseActivity
from trackers.food.objects.food_entry import FoodEntry
import re

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Tracker:

    def __init__(self):
        self.exercise_tracker_list = []
        self.vet_tracker_list = []
        self.food_tracker_list = []

    def addExerciseTracker(self):
        while True:
            type_input = input("Enter exercise type: ")
            if not type_input:
                print("Exercise type cannot be empty. Please try again.")
                continue

            intensity_level_input = input("Enter intensity level from 1 - 10: ")
            if not intensity_level_input.isdigit() or not (1 <= int(intensity_level_input) <= 10):
                print("Intensity level must be a number between 1 and 10. Please try again.")
                continue

            duration_input = input("Enter duration in minutes: ")
            if not duration_input.isdigit() or int(duration_input) <= 0:
                print("Duration must be a positive number. Please try again.")
                continue

            break

        new_exercise = ExerciseActivity(type_input, intensity_level_input, duration_input)
        self.exercise_tracker_list.append(new_exercise)

    import re

    def addVetTracker(self):
        while True:
            visit_date_input = input("Enter visit date (YYYY-MM-DD): ")
            if not re.match(r'\d{4}-\d{2}-\d{2}', visit_date_input):
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            reason_input = input("Enter reason for visit: ")
            if not reason_input:
                print("Reason for visit cannot be empty. Please try again.")
                continue

            vet_name_input = input("Enter vet's name: ")
            if not vet_name_input:
                print("Vet's name cannot be empty. Please try again.")
                continue

            break

        new_vet_visit = VetVisit(visit_date_input, reason_input, vet_name_input)
        self.vet_tracker_list.append(new_vet_visit)

        def addFoodTracker(self):
            while True:
                food_type_input = input("Enter food type: ")
                if not food_type_input:
                    print("Food type cannot be empty. Please try again.")
                    continue

                quantity_input = input("Enter quantity in grams: ")
                if not quantity_input.isdigit() or int(quantity_input) <= 0:
                    print("Quantity must be a positive number. Please try again.")
                    continue

                feeding_time_input = input("Enter feeding time (HH:MM): ")
                if not re.match(r'\d{2}:\d{2}', feeding_time_input):
                    print("Invalid time format. Please use HH:MM.")
                    continue

                break

            new_food_entry = FoodEntry(food_type_input, quantity_input, feeding_time_input)
            self.food_tracker_list.append(new_food_entry)

    def print_all_trackers(self, dogname):
        print(f"######### Tracker Log for : {dogname} #########")

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

# Example usage:
# Create an instance of your class (assuming it's named DogTracker)
# tracker = DogTracker()
# Call the function to print all lists
# tracker.print_all_trackers()
    def to_dict(self):
        """Convert class attributes to a dictionary."""
        return {
            "exercise_tracker_list": [exercise.to_dict() for exercise in self.exercise_tracker_list],
            "vet_tracker_list": [vet_visit.to_dict() for vet_visit in self.vet_tracker_list],
            "food_tracker_list": [food_entry.to_dict() for food_entry in self.food_tracker_list]
        }



    def to_json(self):
        """Convert class attributes to JSON."""
        return json.dumps(self.to_dict(), indent=4)
