class Player:
    def __init__(self, last_name, first_name, birth_date, chess_id, score=0.0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = score

    def update_score(self, points):
        """Add points to the player's score."""
        self.score += points

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["last_name"],
            data["first_name"],
            data["birth_date"],
            data["chess_id"],
            data["score"]
        )
