import json

class ExerciseActivity:

    def __init__(self, type: str, duration: int, intensity_level: int):
        self.type = type
        self.duration = duration
        self.intensity_level = intensity_level

    def __str__(self):
        return f"{self.type} - {self.duration} - {self.intensity_level}"

    def to_dict(self):
        """Convert class attributes to a dictionary."""
        return {
            "type": self.type,
            "duration": self.duration,
            "intensity_level": self.intensity_level
        }



    def to_json(self):
        """Convert class attributes to JSON."""
        return json.dumps(self.to_dict(), indent=4)
