import os
import json

from models.player import Player
from models.tournament import Tournament
from views.menu_view import MenuView


class TournamentController:
    def __init__(self):
        # Par défaut, on démarre un nouveau tournoi vierge
        self.tournoi = Tournament(
            nom="Tournoi Test",
            localisation="Paris",
            date_debut="2025-07-20",
            date_fin="2025-07-21",
            description="Tournoi d'entraînement"
        )

    def run(self):
        """Boucle principale du menu"""
        while True:
            MenuView.afficher_menu()
            choix = input("\nVotre choix : ")

            if choix == "1":
                # === Ajouter un joueur ===
                nom, prenom, date_naissance, chess_id = MenuView.demander_info_joueur()
                joueur = Player(nom, prenom, date_naissance, chess_id)
                self.tournoi.add_players([joueur])
                MenuView.afficher_message(f"✅ Joueur {joueur.nom} {joueur.prenom} ajouté avec succès.")

            elif choix == "2":
                # === Liste des joueurs ===
                MenuView.afficher_titre("Liste des joueurs")
                MenuView.afficher_joueurs(self.tournoi.players)

            elif choix == "3":
                # === Lancer un round ===
                MenuView.afficher_titre("Lancer un round")
                if len(self.tournoi.players) < 2:
                    MenuView.afficher_message("⚠ Pas assez de joueurs pour lancer un round (minimum 2).")
                else:
                    self.tournoi.start_round()
                    MenuView.afficher_message("✅ Round démarré avec succès.")

            elif choix == "4":
                # === Clôturer le round en cours ===
                if not self.tournoi.rounds:
                    MenuView.afficher_message("⚠ Aucun round à clôturer, lancez un round d'abord.")
                else:
                    MenuView.afficher_titre("Clôture du round en cours")
                    self.tournoi.end_round()

            elif choix == "5":
                # === Historique des rounds ===
                MenuView.afficher_titre("Historique des rounds")
                MenuView.afficher_historique(self.tournoi.rounds)

            elif choix == "6":
                # === Classement des joueurs ===
                MenuView.afficher_titre("Classement des joueurs")
                classement = sorted(self.tournoi.players, key=lambda p: p.score, reverse=True)
                MenuView.afficher_classement(classement)

            elif choix == "7":
                # === Sauvegarder le tournoi ===
                self.sauvegarder_tournoi()

            elif choix == "8":
                # === Charger un tournoi existant ===
                self.charger_tournoi()

            elif choix == "9":
                MenuView.afficher_message("Au revoir !")
                break

            else:
                MenuView.afficher_message("❌ Choix invalide, essayez encore.")

    def sauvegarder_tournoi(self):
        """Sauvegarder le tournoi dans saves/"""
        if not os.path.exists("saves"):
            os.makedirs("saves")

        filename = input("Nom du fichier de sauvegarde (ex: tournoi_paris.json) : ")
        if not filename.endswith(".json"):
            filename += ".json"

        path = os.path.join("saves", filename)

        with open(path, "w") as f:
            json.dump(self.tournoi.to_dict(), f, indent=2)

        MenuView.afficher_message(f"✅ Tournoi sauvegardé dans {path}")

    def charger_tournoi(self):
        """Lister et charger un tournoi sauvegardé depuis saves/"""
        if not os.path.exists("saves"):
            os.makedirs("saves")

        fichiers = [f for f in os.listdir("saves") if f.endswith(".json")]

        if not fichiers:
            MenuView.afficher_message("⚠ Aucun tournoi sauvegardé trouvé dans saves/")
            return

        MenuView.afficher_titre("Tournois disponibles")
        for i, f in enumerate(fichiers, start=1):
            print(f"{i}. {f}")

        choix_fichier = int(input("Quel tournoi charger ? (numéro) : "))
        if 1 <= choix_fichier <= len(fichiers):
            filename = os.path.join("saves", fichiers[choix_fichier - 1])
            with open(filename, "r") as f:
                data = json.load(f)
            self.tournoi = Tournament.from_dict(data)
            MenuView.afficher_message(f"✅ Tournoi '{self.tournoi.nom}' chargé avec succès !")
        else:
            MenuView.afficher_message("❌ Numéro invalide.")
