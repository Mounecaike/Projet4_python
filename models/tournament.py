import random
from models.match import Match
from models.round import Round
from models.player import Player


class Tournament:
    """Manages a tournament: players, rounds, and main logic."""
    def __init__(self, name, location, start_date, end_date, description,
                 rounds=None, players=None):
        """
        rounds & players are optional (useful for loading a tournament).
        By default, they are initialized as empty lists.
        """
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.rounds = rounds if rounds is not None else []
        self.players = players if players is not None else []

    def add_players(self, new_players):
        """Add a list of players to the tournament."""
        self.players.extend(new_players)

    def start_round(self):
        """Start a new round and randomly generate matches."""
        round_number = len(self.rounds) + 1
        round_name = f"Round {round_number}"

        new_round = Round(
            name=round_name,
            start_time="2025-07-15 14:00"
        )

        # Shuffle players to create random pairs
        shuffled_players = self.players[:]
        random.shuffle(shuffled_players)

        for i in range(0, len(shuffled_players), 2):
            p1 = shuffled_players[i]
            p2 = shuffled_players[i + 1]
            match = Match(p1, p2, 0, 0)
            new_round.matches.append(match)

        self.rounds.append(new_round)

    def end_round(self):
        """Close the last round by recording scores and end time."""
        if not self.rounds:
            print("⚠ No round has started yet.")
            return

        current_round = self.rounds[-1]
        print(f"\n=== Closing {current_round.name} ===")

        for match in current_round.matches:
            print(f"\nMatch: {match.player1.last_name} vs {match.player2.last_name}")

            score1 = float(input(f"Score for {match.player1.last_name}: "))
            score2 = float(input(f"Score for {match.player2.last_name}: "))

            match.set_result(score1, score2)

            match.player1.update_score(score1)
            match.player2.update_score(score2)

        current_round.end_round("2025-07-15 16:00")
        print(f"✅ {current_round.name} finished at {current_round.end_time}")

    def to_dict(self):
        """Convert the tournament to a dictionary"""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "players": [p.to_dict() for p in self.players],
            "rounds": [r.to_dict() for r in self.rounds]
        }

    @classmethod
    def from_dict(cls, data):
        """Recreate a complete tournament from a JSON dict."""
        players = [Player.from_dict(p) for p in data["players"]]
        rounds = [Round.from_dict(r) for r in data["rounds"]]

        return cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data["description"],
            rounds=rounds,
            players=players
        )
