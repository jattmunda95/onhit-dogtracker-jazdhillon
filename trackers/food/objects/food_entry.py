import json

class FoodEntry:
    def __init__(self, food_type, quantity, feeding_time):
        self.food_type = food_type
        self.quantity = quantity
        self.feeding_time = feeding_time

    def __str__(self):
        return f"FoodEntry(type={self.food_type}, quantity={self.quantity}g, time={self.feeding_time})"

    def to_dict(self):
        """Convert class attributes to a dictionary."""
        return {
            "food_type": self.food_type,
            "quantity": self.quantity,
            "feeding_time": self.feeding_time
        }



    def to_json(self):
        """Convert class attributes to JSON."""
        return json.dumps(self.to_dict(), indent=4)
