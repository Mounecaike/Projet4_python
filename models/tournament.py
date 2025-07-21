import random
from models.match import Match
from models.round import Round


class Tournament:
    def __init__(self, nom, localisation, date_debut, date_fin, description,
                 rounds=None, players=None):
        """
        rounds & players sont optionnels (utiles pour recharger un tournoi).
        Par défaut, ils sont initialisés comme des listes vides.
        """
        self.nom = nom
        self.localisation = localisation
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.description = description
        self.rounds = rounds if rounds is not None else []
        self.players = players if players is not None else []

    def add_players(self, new_players):
        """Ajoute une liste de joueurs au tournoi."""
        self.players.extend(new_players)

    def start_round(self):
        """Démarre un nouveau round et génère les matchs aléatoirement."""
        round_number = len(self.rounds) + 1
        round_name = f"Round {round_number}"

        new_round = Round(
            name=round_name,
            start_time="2025-07-15 14:00"
        )

        # Mélanger les joueurs pour créer des paires aléatoires
        shuffled_players = self.players[:]
        random.shuffle(shuffled_players)

        for i in range(0, len(shuffled_players), 2):
            p1 = shuffled_players[i]
            p2 = shuffled_players[i + 1]
            match = Match(p1, p2, 0, 0)
            new_round.matches.append(match)

        self.rounds.append(new_round)

    def end_round(self):
        """Clôture le dernier round en enregistrant les scores et l'heure de fin."""
        if not self.rounds:
            print("⚠ Aucun round n’a encore commencé.")
            return

        # Récupérer le round en cours
        current_round = self.rounds[-1]
        print(f"\n=== Clôture de {current_round.name} ===")

        for match in current_round.matches:
            print(f"\nMatch : {match.player1.nom} vs {match.player2.nom}")

            # Saisie manuelle des scores
            score1 = float(input(f"Score de {match.player1.nom} : "))
            score2 = float(input(f"Score de {match.player2.nom} : "))

            # Mise à jour du match
            match.set_result(score1, score2)

            # Mise à jour des scores cumulés des joueurs
            match.player1.update_score(score1)
            match.player2.update_score(score2)

        # Clôture officielle du round
        current_round.end_round("2025-07-15 16:00")
        print(f"✅ {current_round.name} terminé à {current_round.end_time}")

    def to_dict(self):
        """Convertit le tournoi en dictionnaire"""
        return {
            "nom": self.nom,
            "localisation":self.localisation,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "description": self.description,
            "players": [p.to_dict() for p in self.players],
            "rounds": [r.to_dict() for r in self.rounds]
        }