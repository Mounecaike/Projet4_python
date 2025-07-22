class MenuView:

    @staticmethod
    def afficher_menu():
        print("\n=== MENU PRINCIPAL ===")
        print("1. Ajouter un joueur")
        print("2. Lister les joueurs")
        print("3. Lancer un round")
        print("4. Clôturer le dernier round")
        print("5. Voir l’historique des rounds")
        print("6. Voir le classement des joueurs")
        print("7. Sauvegarder le tournoi")
        print("8. Charger un tournoi existant")
        print("9. Quitter")

    @staticmethod
    def demander_info_joueur():
        nom = input("Nom du joueur : ")
        prenom = input("Prénom du joueur : ")
        date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
        chess_id = input("Identifiant FIDE : ")
        return nom, prenom, date_naissance, chess_id

    @staticmethod
    def afficher_joueurs(players):
        """Affiche la liste des joueurs"""
        if not players:
            print("⚠ Aucun joueur enregistré.")
        else:
            for p in players:
                print(f" - {p.nom} {p.prenom} ({p.chess_id}) | Score : {p.score}")

    @staticmethod
    def afficher_historique(rounds):
        """Affiche tous les rounds joués avec leurs matchs"""
        if not rounds:
            print("⚠ Aucun round joué pour le moment.")
        else:
            for r in rounds:
                print(f"\n{r.name} | Début : {r.start_time} | Fin : {r.end_time or 'en cours...'}")
                for m in r.matches:
                    print(f"  - {m.player1.nom} ({m.score1}) vs {m.player2.nom} ({m.score2})")

    @staticmethod
    def afficher_classement(players):
        """Affiche un classement des joueurs"""
        if not players:
            print("⚠ Aucun joueur enregistré.")
        else:
            for i, p in enumerate(players, start=1):
                print(f"{i}. {p.nom} {p.prenom} ({p.chess_id}) | Score : {p.score}")

    @staticmethod
    def afficher_message(message):
        """Affiche un message générique"""
        print(message)

    @staticmethod
    def afficher_titre(titre):
        """Affiche un titre formaté"""
        print(f"\n=== {titre} ===")
