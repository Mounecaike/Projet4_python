class Player:
    def __init__(self, nom, prenom, date_naissance, chess_id, score=0.0):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.chess_id = chess_id
        self.score = score

    def update_score(self, points):
        """Ajoute des points au score du joueur."""
        self.score += points

    def to_dict(self):
        """Retourne une représentation dict du joueur."""
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date de naissance": self.date_naissance,
            "chess_id": self.chess_id,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un joueur à partir d’un dict."""
        return cls(
            data["nom"],
            data["prenom"],
            data["date de naissance"],
            data["chess_id"],
            data["score"]
        )
