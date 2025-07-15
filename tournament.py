from models.match import Match
from models.round import Round
import random
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

    def start_round (self) :
        round_number = len(self.rounds) + 1
        round_name = f"Round {round_number}"
        new_round = Round(name=round_name, start_time= "2025-07-15 14:00")

        shuffled_players = self.players[:]
        random.shuffle(shuffled_players)

        for i in range(0, len(shuffled_players), 2):
            p1 = shuffled_players[i]
            p2 = shuffled_players[i+1]
            match = Match(p1, p2, 0, 0)
            new_round.matches.append(match)

        self.rounds.append(new_round)

