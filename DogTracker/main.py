import sys
import os
import json
import time

from dog import Dog
from trackers.food.objects.food_entry import FoodEntry
from trackers.vet.objects.vet_visits import VetVisit
from trackers.exercise.objects.exercise_activity import ExerciseActivity

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

dog_dict = {}


def dog_exist(dog_name: str) -> bool:
    """Check if a dog exists in the dog_dict."""
    dog_name = dog_name.lower()
    return dog_name in dog_dict


def add_dog() -> None:
    """
    a static method to add a dog object to the dictionary of dogs
    :return: None
    """
    while True:
        dog_name = input("Please enter dog name to make new entry: ").lower()
        if dog_name not in dog_dict and dog_name.isalpha():
            dog_size = input("Enter your dog's size?\n"
                             "small | medium | large\n").lower()
            dog_gender = input("Enter your dog's gender [m/f]: ").lower()
            new_dog = Dog(dog_name, dog_size, dog_gender)
            dog_dict[dog_name] = new_dog
            print(f"Dog Dict looks like this now:\n")
            for dog_name, dog in dog_dict.items():
                print(f"\t{dog_name}: {dog}")
            break
        else:
            print("=" * 10 + "ERROR" + "=" * 10)
            print(f"Dog name {dog_name} already exists or is invalid. Please try again.")
            print("\n" * 2)
            continue


def get_valid_number(prompt: str, min_value: int = None, max_value: int = None) -> int:
    """Prompt the user for a valid number within an optional range."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}. Please try again.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def exercise_entry_menu() -> None:
    while True:
        dog_name = input("Which dog to add entry for:\n").lower()
        print(f"Which exercise activity do you wish to use? >{dog_name}<")

        if dog_exist(dog_name):
            dog = dog_dict.get(dog_name)
            input_type = input("Which type of exercise?\n").lower()
            input_intensity = get_valid_number("What was the intensity of exercise [1 to 10]?\n", 1, 10)
            input_duration = get_valid_number("What was the duration of exercise?\n", 1)
            new_exercise_obj = ExerciseActivity(input_type, input_duration, input_intensity)
            dog.tracker.exercise_tracker_list.append(new_exercise_obj)
            break
        else:
            print("Dog does not exist, TRY AGAIN")
            input("Press Enter to continue...")


def vet_entry_menu() -> None:
    while True:
        dog_name = input("For which dog do you want to add a vet entry for:\n").lower()
        if dog_exist(dog_name):
            input_visit_date = input("What was the date of visit?\n").lower()
            input_reason = input("What was the reason of visit?\n").lower()
            input_outcome = input("What was the outcome of visit?\n").lower()
            input_vet_name = input("What was the name of vet?\n").lower()
            dog = dog_dict.get(dog_name)
            new_vet_obj = VetVisit(input_visit_date, input_reason, input_outcome, input_vet_name)
            dog.tracker.vet_tracker_list.append(new_vet_obj)
            break
        else:
            print("Dog does not exist, TRY AGAIN")
            input("Press Enter to continue...")


def food_entry_menu() -> None:
    while True:
        dog_name = input("For which dog do you want to add a food entry for:\n").lower()
        if dog_exist(dog_name):
            food_type = input("Which type of food?\n").lower()
            food_quantity = get_valid_number("How much food did you feed in grams?\n", 1)
            feeding_time = input("What was the time of feeding?\nMorning [m]\nAfternoon [a]\nEvening [e]\n").lower()
            dog = dog_dict.get(dog_name)
            new_food_obj = FoodEntry(food_type, food_quantity, feeding_time)
            dog.tracker.food_tracker_list.append(new_food_obj)
            break
        else:
            print("Dog does not exist, TRY AGAIN")
            input("Press Enter to continue...")


def save_to_json_file():
    """Save dog data to a JSON file and measure the time it takes."""
    start_time = time.time()  # Start the timer

    # Initialize dictionary for JSON conversion
    dog_dict_json = {}
    # Convert each Dog object to a dictionary and add to dog_dict_json
    for name, dog in dog_dict.items():
        dog_dict_json[name] = dog.to_dict()

    # Save the dictionary to a JSON file
    with open('dog_tracker_data.json', 'w') as json_file:
        json.dump(dog_dict_json, json_file, indent=4)

    # Measure the elapsed time for saving
    elapsed_time = time.time() - start_time
    print(f"Information saved successfully. Time taken to save: {elapsed_time:.4f} seconds.")


def load_dog_data_from_json(file_path):
    """Load dog data from a JSON file and measure the time it takes."""
    start_time = time.time()  # Start the timer

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    dog_data_holder = {}
    for name, dog_data in data.items():
        dog_data_holder[name] = Dog.from_dict(dog_data)

    # Measure the elapsed time for loading
    elapsed_time = time.time() - start_time
    print(f"Time taken to load dog data: {elapsed_time:.4f} seconds.")

    return dog_data_holder


def main():
    global dog_dict

    # load JSON data to memory on initialization
    file_path = 'dog_tracker_data.json'  # Path to your JSON file
    dog_dict = load_dog_data_from_json(file_path).copy()

    for name, dog in dog_dict.items():
        print("name: {}, dog: {}".format(name.lower(), dog))

    while True:
        # Welcome dialog
        print(f"Welcome to the KAI9 App :-)")

        # Menu options
        action_choice = input(f"What would you like to look at?\n"
                              "=> Food Menu [f]\n"
                              "=> Vet Information [v]\n"
                              "=> Exercise Tracker [e]\n"
                              "=> Add Your Dogs [d]\n"
                              "=> Print Tracker Log [s]\n"
                              "=> Save Info [x]\n"
                              "=> Quit [q]\n").lower()

        if action_choice == "d":
            add_dog()

        elif action_choice == "f":
            food_entry_menu()

        elif action_choice == "v":
            vet_entry_menu()

        elif action_choice == "e":
            exercise_entry_menu()

        elif action_choice == "s":
            for dog_name, dog_obj in dog_dict.items():
                dog_obj.dog_details()

        elif action_choice == "x":
            save_to_json_file()

        elif action_choice == "q":
            break


# Main loop execution on file run
if __name__ == "__main__":
    main()
