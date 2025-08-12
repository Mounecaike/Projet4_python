class MenuView:
    """Handles all console menus and user prompts."""

    @staticmethod
    def show_pre_menu():
        """Displays the welcome pre-menu."""
        print("\n--- Welcome to Tournament Manager ---\n")
        print("1.Create a new tournament")
        print("2. Load an existing tournament")
        print("3. Exit")

    @staticmethod
    def show_menu():
        """Displays the main menu."""
        print("\n=== MAIN MENU ===")
        print("1. Manage players")
        print("2. Manage rounds")
        print("3. Generate tournament report")
        print("4. save the tournament")
        print("5. Load an existing tounament")
        print("6. Exit")

    @staticmethod
    def show_player_menu():
        """Displays the player management submenu."""
        print("\n=== MANAGE PLAYERS ===")
        print("1. Add a player")
        print("2. List all players")
        print("3. Show ranking")
        print("4. Return to main menu")

    @staticmethod
    def show_round_menu():
        """Displays the round management submenu."""
        print("\n=== MANAGE ROUNDS ===")
        print("1. Start a round")
        print("2. Close current round")
        print("3. Show rounds history")
        print("4. Return to main menu")

    @staticmethod
    def ask_player_info():
        """Asks the user to enter player details."""
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
