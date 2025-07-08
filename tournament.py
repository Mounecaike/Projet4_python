class Tournament :
    def __init__(self, nom, localisation, date_debut, date_fin, description, rounds, players):
        self.nom = nom
        self.localisation = localisation
        self.date_debut = date_debut
        self. date_fin = date_fin
        self.description = description
        self.rounds = []
        self.players = []

    def add_players (self, new_players):
        self.players.extend(new_players)

    def start_round (self, rounds) :
        