class Player :

    def __init__(self, nom, prenom, date_naissance, chess_id, score=0.0):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.chess_id = chess_id
        self.score = score

    def update_score(self, points):
        self.score += points

    def to_dict(self):
        return {
            "nom" : self.nom,
            "prenom" : self.prenom,
            "date de naissance": self.date_naissance,
            "chess_id" : self.chess_id,
            "score" : self.score
        }

    @classmethod
    def from_dict(cls, data):
        return cls (
            data["nom"],
            data["prenom"],
            data["date de naissance"],
            data["chess_id"],
            data["score"]
        )
