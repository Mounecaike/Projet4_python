class Match:
    def __init__(self, player1, player2, score1, score2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def set_result(self, score1, score2):
        """Met à jour les scores du match."""
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        """Retourne une version simplifiée du match pour sauvegarde."""
        return (
            [self.player1.chess_id, self.score1],
            [self.player2.chess_id, self.score2]
        )

    @classmethod
    def from_dict(cls, data):
        """Recrée un match à partir d’un dict (à adapter si besoin)."""
        return cls(
            data["player1"],
            data["player2"],
            data["score1"],
            data["score2"]
        )
