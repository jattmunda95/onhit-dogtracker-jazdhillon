import json

class VetVisit:
    """
    Represents a veterinary visit record.

    This class is used to store and manage information about a specific visit to a veterinarian,
    including the date, reason for the visit, outcome of the visit, and the veterinarian's name.

    Attributes
    ----------
    visit_date : str
        The date of the vet visit in the format YYYY-MM-DD.
    reason : str
        The reason for the visit (e.g., check-up, vaccination, etc.).
    outcome : str
        The outcome of the visit (e.g., treatment provided, recovery status).
    vet_name : str
        The name of the veterinarian handling the visit.

    Methods
    -------
    __str__():
        Returns a string representation of the VetVisit instance.
    from_dict(data: dict):
        Class method to create a VetVisit instance from a dictionary.
    to_dict():
        Converts the VetVisit instance attributes into a dictionary.
    to_json():
        Converts the VetVisit instance into a JSON string representation.
    """

    def __init__(self, visit_date: str, reason: str, outcome: str, vet_name: str):
        """
        Initializes a VetVisit instance.

        Parameters
        ----------
        visit_date : str
            The date of the vet visit in the format YYYY-MM-DD.
        reason : str
            The reason for the visit.
        outcome : str
            The outcome of the visit.
        vet_name : str
            The name of the veterinarian attending to the visit.
        """
        self.visit_date = visit_date
        self.reason = reason
        self.outcome = outcome
        self.vet_name = vet_name

    def __str__(self) -> str:
        """
        Returns a string representation of the VetVisit instance.

        The string format is:
        "VetVisit {visit_date} {reason} {outcome} {vet_name}"

        :returns: A string representation of the VetVisit instance.
        :rtype: str
        """
        return f"VetVisit {self.visit_date} {self.reason} {self.outcome} {self.vet_name}"

    @classmethod
    def from_dict(cls, data: dict) -> 'VetVisit':
        """
        Creates a VetVisit instance from a dictionary.

        This class method parses the provided dictionary to extract the required attributes
        and initializes a new VetVisit instance.

        Parameters
        ----------
        data : dict
            A dictionary containing the following keys:
            - 'visit_date': The date of the visit.
            - 'reason': The reason for the visit.
            - 'outcome': The outcome of the visit.
            - 'vet_name': The name of the veterinarian.

        :returns: A new VetVisit instance.
        :rtype: VetVisit
        """
        return cls(data["visit_date"], data["reason"], data["outcome"], data["vet_name"])

    def to_dict(self) -> dict:
        """
        Converts the VetVisit instance attributes to a dictionary.

        This method creates a dictionary representation of the VetVisit instance, making it
        easier to serialize or transfer data in dictionary form.

        :returns: A dictionary representation of the VetVisit instance.
        :rtype: dict
        """
        return {
            "visit_date": self.visit_date,
            "reason": self.reason,
            "outcome": self.outcome,
            "vet_name": self.vet_name
        }

    def to_json(self) -> str:
        """
        Converts the VetVisit instance to a JSON string.

        This method serializes the VetVisit instance by first converting it to a dictionary
        and then serializing it into a JSON-formatted string.

        :returns: A JSON string representation of the VetVisit instance.
        :rtype: str
        """
        return json.dumps(self.to_dict(), indent=4)
