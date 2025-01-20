import json

class VetVisit:
    def __init__(self, visit_date, reason, outcome, vet_name):
        self.visit_date = visit_date
        self.reason = reason
        self.outcome = outcome
        self.vet_name = vet_name

    def __str__(self):
        return f"VetVisit {self.visit_date} {self.reason} {self.outcome} {self.vet_name}"

    @classmethod
    def from_dict(cls, data):
        return cls(data["visit_date"], data["reason"], data["outcome"], data["vet_name"])

    def to_dict(self):
        """Convert class attributes to a dictionary."""
        return {
            "visit_date": self.visit_date,
            "reason": self.reason,
            "outcome": self.outcome,
            "vet_name": self.vet_name
        }

    def to_json(self):
        """Convert class attributes to JSON."""
        return json.dumps(self.to_dict(), indent=4)
