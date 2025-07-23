class Round:
    def __init__(self, name, start_time, end_time=None, matches=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches if matches else []

    def end_round(self, end_time):
        """Mark the round as finished by adding the end date/time."""
        self.end_time = end_time

    def to_dict(self):
        """Return a dict with round information."""
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [match.to_dict() for match in self.matches]
        }

    @classmethod
    def from_dict(cls, data):
        """Create a round from a dict."""
        return cls(
            data["name"],
            data["start_time"],
            data["end_time"],
            data["matches"]
        )
