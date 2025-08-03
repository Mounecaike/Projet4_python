class Match:
    def __init__(self, player1, player2, score1, score2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def set_result(self, score1, score2):
        """Update match scores."""
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        """Return a simplified match representation for saving."""
        return (
            [self.player1.chess_id, self.score1],
            [self.player2.chess_id, self.score2]
        )

    @classmethod
    def from_dict(cls, data):
        """
        Recreate a match from a list like:
        [[player1_id, score1], [player2_id, score2]]
        """
        player1_id, score1 = data[0]
        player2_id, score2 = data[1]
        return cls(player1_id, player2_id, score1, score2)

