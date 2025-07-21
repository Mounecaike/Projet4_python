from models.player import Player
from models.tournament import Tournament


def afficher_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Ajouter un joueur")
    print("2. Lister les joueurs")
    print("3. Lancer un round")
    print("4. Clôturer le dernier round")
    print("5. voir l'historique des rounds")
    print("6. Voir le classement des joueurs")
    print("7. Sauvegarder le tournoi")
    print("8. Quitter")

def main():
    """Création du tournois"""
    tournoi = Tournament(
        nom="Tournois test",
        localisation="Paris",
        date_debut="2025-07-20",
        date_fin="2025-07-21",
        description="Tournoi d'entraînement"
    )


    while True:
        afficher_menu()
        choix = input("\nVotre choix : ")

        if choix == "1":
            print("\n=== Ajouter un joueur ===")
            nom = input("nom du joueur: ")
            prenom = input("Prénom du joueur: ")
            date_naissance = input("Date de naissance (DD-MM-YYYY): ")
            chess_id = input("Identifiant FIDE: ")

            joueur = Player(nom, prenom, date_naissance, chess_id)
            tournoi.add_players([joueur])

            print(f"✅ Joueur {joueur.nom} {joueur.prenom} ajouté avec succès.")
        elif choix == "2":
            print("\n=== Liste des joueurs ===")
            if not tournoi.players :
                print("Aucun joueur enregistrer")
            else:
                for p in tournoi.players:
                    print(f" - {p.nom} {p.prenom} ({p.chess_id}) | Score : {p.score}")
        elif choix == "3":
            print("\n=== Lancer un round ===")
            if len(tournoi.players) < 2:
                print("Pas assez de joueur pour lancer un round (minimum 2)")
            else:
                tournoi.start_round()
                print("Round démarré avec succès.")
        elif choix == "4":
            if not tournoi.rounds :
                print("aucun round à clôturer, lancez un round d'abord.")
            else:
                print("\n=== clôture du round en cours ===")
                tournoi.end_round()
        elif choix == "5":
            print("\n=== Historique des rounds ===")
            if not tournoi.rounds:
                print("Aucun round joué pour le moment")
            else:
                for r in tournoi.rounds:
                    print(f"\n {r.name} | début : {r.start_time} | fin : {r.end_time or 'en cours...'}")
                    for m in r.matches:
                        print(f"  - {m.player1.nom} ({m.score1}) vs {m.player2.nom} ({m.score2})")
        elif choix == "6":
            print("\n=== Classement des joueurs ===")
            if not tournoi.players:
                print("Aucun joueur enregistré.")
            else:
                classement = sorted(tournoi.players, key=lambda p: p.score, reverse=True)
                for i, p in enumerate(classement, start=1):
                    print(f"{i}. {p.nom} {p.prenom} ({p.chess_id}) | Score : '{p.score}")
        elif choix == "7":
            import json
            filename = input("nom du fichier de sauvegarde (ex: tounoi_paris.json: ")
            if not filename.endswith(".json"):
                filename +=".json"
            with open(filename, "w") as f:
                json.dump(tournoi.to_dict(), f, indent=2)
            print(f"Tournoi sauvegarder dans {filename}")
        elif choix == "8":
            print("Au revoir !")
            break
        else:
            print("❌ Choix invalide, essayez encore.")

if __name__ == "__main__":
    main()
