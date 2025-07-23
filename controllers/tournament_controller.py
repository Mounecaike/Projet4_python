import os
import json

from models.player import Player
from models.tournament import Tournament
from views.menu_view import MenuView


class TournamentController:
    def __init__(self):
        # By default, start a new blank tournament
        self.tournament = Tournament(
            name="Test Tournament",
            location="Paris",
            start_date="2025-07-20",
            end_date="2025-07-21",
            description="Training tournament"
        )

    def run(self):
        """Main menu loop"""
        while True:
            MenuView.show_menu()
            choice = input("\nYour choice: ")

            if choice == "1":
                # === Add a player ===
                last_name, first_name, birth_date, chess_id = MenuView.ask_player_info()
                player = Player(last_name, first_name, birth_date, chess_id)
                self.tournament.add_players([player])
                MenuView.show_message(f"✅ Player {player.last_name} {player.first_name} added successfully.")
                self.auto_save()  # ✅ auto-save after adding player

            elif choice == "2":
                # === List all players ===
                MenuView.show_title("Players list")
                MenuView.show_players(self.tournament.players)

            elif choice == "3":
                # === Start a round ===
                MenuView.show_title("Start a round")
                if len(self.tournament.players) < 2:
                    MenuView.show_message("⚠ Not enough players to start a round (minimum 2).")
                else:
                    self.tournament.start_round()
                    MenuView.show_message("✅ Round started successfully.")
                    self.auto_save()  # ✅ auto-save after starting a round

            elif choice == "4":
                # === Close the current round ===
                if not self.tournament.rounds:
                    MenuView.show_message("⚠ No round to close, start a round first.")
                else:
                    MenuView.show_title("Closing current round")
                    self.tournament.end_round()
                    self.auto_save()  # ✅ auto-save after ending a round

            elif choice == "5":
                # === Rounds history ===
                MenuView.show_title("Rounds history")
                MenuView.show_rounds_history(self.tournament.rounds)

            elif choice == "6":
                # === Player ranking ===
                MenuView.show_title("Player ranking")
                ranking = sorted(self.tournament.players, key=lambda p: p.score, reverse=True)
                MenuView.show_ranking(ranking)

            elif choice == "7":
                # === Save the tournament ===
                self.save_tournament()

            elif choice == "8":
                # === Load an existing tournament ===
                self.load_tournament()

            elif choice == "9":
                MenuView.show_message("Goodbye!")
                break

            elif choice == "10":
                # ✅ NEW → Show full tournament report
                self.show_report()

            else:
                MenuView.show_message("❌ Invalid choice, try again.")

    # ✅ AUTO-SAVE
    def auto_save(self):
        """Auto-save the tournament after each critical action"""
        if not os.path.exists("saves"):
            os.makedirs("saves")
        path = os.path.join("saves", "autosave.json")
        with open(path, "w") as f:
            json.dump(self.tournament.to_dict(), f, indent=2)
        print("💾 Auto-saved tournament to saves/autosave.json")

    def save_tournament(self):
        """Save the tournament manually in saves/"""
        if not os.path.exists("saves"):
            os.makedirs("saves")

        filename = input("Save file name (e.g. paris_tournament.json): ")
        if not filename.endswith(".json"):
            filename += ".json"

        path = os.path.join("saves", filename)

        with open(path, "w") as f:
            json.dump(self.tournament.to_dict(), f, indent=2)

        MenuView.show_message(f"✅ Tournament saved in {path}")

    def load_tournament(self):
        """List and load a saved tournament from saves/"""
        if not os.path.exists("saves"):
            os.makedirs("saves")

        files = [f for f in os.listdir("saves") if f.endswith(".json")]

        if not files:
            MenuView.show_message("⚠ No saved tournament found in saves/")
            return

        MenuView.show_title("Available tournaments")
        for i, f in enumerate(files, start=1):
            print(f"{i}. {f}")

        file_choice = int(input("Which tournament to load? (number): "))
        if 1 <= file_choice <= len(files):
            filename = os.path.join("saves", files[file_choice - 1])
            with open(filename, "r") as f:
                data = json.load(f)
            self.tournament = Tournament.from_dict(data)
            MenuView.show_message(f"✅ Tournament '{self.tournament.name}' loaded successfully!")
        else:
            MenuView.show_message("❌ Invalid number.")

    def show_report(self):
        """Display a complete tournament report"""
        t = self.tournament

        MenuView.show_title("Tournament Report")
        print(f"Name: {t.name}")
        print(f"Location: {t.location}")
        print(f"Dates: {t.start_date} → {t.end_date}")
        print(f"Description: {t.description}")
        print(f"Number of players: {len(t.players)}")

        print("\n--- Players ---")
        for p in t.players:
            print(f"- {p.last_name} {p.first_name} ({p.chess_id}) | Score: {p.score}")

        print("\n--- Rounds ---")
        for r in t.rounds:
            print(f"{r.name} | Start: {r.start_time} | End: {r.end_time or 'ongoing...'}")
            for m in r.matches:
                print(f"  - {m.player1.last_name} ({m.score1}) vs {m.player2.last_name} ({m.score2})")

        print("\n--- Final Ranking ---")
        ranking = sorted(t.players, key=lambda p: p.score, reverse=True)
        for i, p in enumerate(ranking, start=1):
            print(f"{i}. {p.last_name} {p.first_name} | {p.score} pts")
