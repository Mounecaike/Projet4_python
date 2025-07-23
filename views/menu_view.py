class MenuView:

    @staticmethod
    def show_menu():
        print("\n=== MAIN MENU ===")
        print("1. Add a player")
        print("2. List players")
        print("3. Start a round")
        print("4. Close the last round")
        print("5. Show rounds history")
        print("6. Show player ranking")
        print("7. Save the tournament")
        print("8. Load an existing tournament")
        print("9. Exit")
        print("10. Show tournament report")

    @staticmethod
    def ask_player_info():
        last_name = input("Player last name: ")
        first_name = input("Player first name: ")
        birth_date = input("Birth date (YYYY-MM-DD): ")
        chess_id = input("FIDE ID: ")
        return last_name, first_name, birth_date, chess_id

    @staticmethod
    def show_players(players):
        """Display the list of players"""
        if not players:
            print("⚠ No players registered.")
        else:
            for p in players:
                print(f" - {p.last_name} {p.first_name} ({p.chess_id}) | Score: {p.score}")

    @staticmethod
    def show_rounds_history(rounds):
        """Display all played rounds with their matches"""
        if not rounds:
            print("⚠ No round played yet.")
        else:
            for r in rounds:
                print(f"\n{r.name} | Start: {r.start_time} | End: {r.end_time or 'ongoing...'}")
                for m in r.matches:
                    print(f"  - {m.player1.last_name} ({m.score1}) vs {m.player2.last_name} ({m.score2})")

    @staticmethod
    def show_ranking(players):
        """Display a ranking of players"""
        if not players:
            print("⚠ No players registered.")
        else:
            for i, p in enumerate(players, start=1):
                print(f"{i}. {p.last_name} {p.first_name} ({p.chess_id}) | Score: {p.score}")

    @staticmethod
    def show_message(message):
        """Display a generic message"""
        print(message)

    @staticmethod
    def show_title(title):
        """Display a formatted title"""
        print(f"\n=== {title} ===")
