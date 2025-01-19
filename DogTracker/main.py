import sys
import os
import json

from dog import Dog
from trackers.food.objects.food_entry import FoodEntry
from trackers.exercise.objects.exercise_activity import ExerciseActivity
from trackers.vet.objects.vet_visits import VetVisit

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

dog_dict = {}

def dog_exist(dog_name: str):
    try:
        value = dog_dict[dog_name]
        return True
    except KeyError:
        print("=" * 10 + "ERROR" + "=" * 10)
        print(f"There are no dogs in the list.\nPlease add a dog first")
        return False

def main():
    while True:
        # welcome dialog
        print(f"Welcome to the KAI9 App :-)")


        # if user has at least one dog listed then they are not prompted to enter new dog instance
        action_choice = input(f"What would you like to look at?\n"
                              "=> Food Menu [f]\n"
                              "=> Vet Information [v]\n"
                              "=> Exercise Tracker [e]\n"
                              "=> Add Your Dogs [d]\n"
                              "=> Print Tracker Log [s]\n"
                              "=> Save Info [x]\n"
                              "=> Quit [q]\n")

        if action_choice == "d":
            dog_name = input("Enter your dog's name [Only letters]: ")
            dog_breed = input("Enter your dog's breed: ")
            dog_gender = input("Enter your dog's gender [M/F]: ")
            new_dog = Dog(dog_name, dog_breed, dog_gender)
            if dog_name not in dog_dict:
                dog_dict[dog_name] = new_dog
                print("the size of the dictionary is: ", len(dog_dict))

            else:
                print("=" * 10 + "ERROR" + "=" * 10)
                print(f"Dog {dog_name} already exists")
                continue

        elif action_choice == "f":
            while True:
                dog_name = input("For which dog do you want to add a food entry for:\n")

                if dog_exist(dog_name):
                    food_type = input(f"Which type of food?\n")
                    food_quantity = input(f"How much food did you feed in grams?\n")
                    feeding_time = input(f"What was the time of feeding?\n"
                                         f"Morning [m]\n"
                                         f"Afternoon [a]\n"
                                         f"Evening [e]\n")
                    dog = dog_dict.get(dog_name)
                    new_food_obj = FoodEntry(food_type, food_quantity, feeding_time)
                    dog.tracker.food_tracker_list.append(new_food_obj)
                    break
                else:
                    print("Dog does not exist, TRY AGAIN")
                    input("Press Enter to continue...")

        elif action_choice == "v":
            while True:
                dog_name = input("For which dog do you want to add a food entry for:\n")
                if dog_exist(dog_name):
                    input_visit_date = input(f"What was the date of visit?\n")
                    input_reason = input(f"What was the reason of visit?\n")
                    input_outcome = input(f"What was the outcome of visit?\n")
                    input_vet_name = input(f"What was the name of vet?\n")
                    dog = dog_dict.get(dog_name)
                    new_vet_obj = VetVisit(input_visit_date, input_reason, input_outcome, input_vet_name)
                    dog.tracker.vet_tracker_list.append(new_vet_obj)
                    break
                else:
                    print("Dog does not exist, TRY AGAIN")
                    input("Press Enter to continue...")

        elif action_choice == "e":
            while True:
                dog_name = input("For which dog do you want to add a exercise entry for:\n")
                if not dog_exist(dog_name):
                    input_type = input(f"Which type of exercise?\n")
                    input_intensity = int(input(f"What was the intensity of exercise [1 to 10]?\n"))
                    input_duration = int(input(f"What was the duration of exercise?\n"))
                    dog = dog_dict.get(dog_name)
                    new_exercise_obj = ExerciseActivity(input_type, input_duration, input_intensity)
                    dog.tracker.vet_tracker_list.append(new_exercise_obj)
                    break
                else:
                    print("Dog does not exist, TRY AGAIN")
                    input("Press Enter to continue...")


        elif action_choice == "s":
            for dog_name, dog_obj in dog_dict.items():
                dog_obj.dog_details(dog_name)

        elif action_choice == "q":
            break

        # Convert dictionary to JSON
        print("before looping")
        dog_dict_json = {name: dog.to_dict() for name, dog in dog_dict.items()}
        print("after looping")
        json_data = json.dumps(dog_dict_json, indent=4)
        # Print JSON string
        print(json_data)

def is_name_unique(dog_list, name):
    names = [dog.name for dog in dog_list]
    return names.count(name) == 1


# main loop execution on file run
if __name__ == "__main__":
    main()
