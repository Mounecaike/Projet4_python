from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament

# === TEST PLAYERS ===
print("=== TEST PLAYERS ===")
player1 = Player("Jean", "Dupont", "1990-01-01", "AB12345")
player2 = Player("Marie", "Durand", "1992-05-12", "CD67890")
player3 = Player("Paul", "Martin", "1991-02-20", "EF13579")
player4 = Player("Lucie", "Lemoine", "1988-11-30", "GH24680")

player1.update_score(1)
player2.update_score(0.5)
print(player1.to_dict())
print(player2.to_dict())

# === TEST TOURNAMENT ===
print("\n=== TEST TOURNAMENT ===")
tournoi = Tournament(
    nom="Tournoi Lyon",
    localisation="Lyon",
    date_debut="2025-07-15",
    date_fin="2025-07-16",
    description="Premier tournoi test",
    rounds=None,
    players=None
)

# Ajouter les joueurs au tournoi
tournoi.add_players([player1, player2, player3, player4])
print(f"Joueurs enregistrés dans le tournoi : {[p.nom for p in tournoi.players]}")

# === TEST START ROUND ===
print("\n=== START ROUND ===")
tournoi.start_round()

# Afficher les infos du round créé
round1 = tournoi.rounds[0]
print(round1.to_dict())

# === TEST END ROUND ===
print("\n=== END ROUND ===")
tournoi.end_round()

# Vérifier les scores des joueurs après le round
print("\nScores après le round :")
for p in tournoi.players:
    print(f"{p.nom} : {p.score} pts")

# Vérifier le round mis à jour
print("\nRound mis à jour :")
print(tournoi.rounds[-1].to_dict())
