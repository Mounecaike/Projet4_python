# Tournament Manager

A Python console application to manage chess tournaments with clean Object-Oriented and MVC architecture.

## Features

- Create and edit tournaments (name, location, dates, description…)
- Add players (unique ID, first name, last name, date of birth…)
- Automatic round generation (random pairings, score input for each match)
- Complete round history and match details
- Player ranking and leaderboard
- Full tournament report (info, players, rounds, ranking…)
- Auto-save and manual save/load of tournaments in JSON format
- Clear menu and submenus (player management, rounds management…)
- Robust navigation, user-friendly messages, safe error handling

## Installation

Clone this repository:
```bash
git clone <your_repo_link>
cd <your_project_folder>
```

(Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
.env\Scriptsctivate     # Windows
```

Install dependencies (not required, but Flake8 is recommended for code style):
```bash
pip install flake8 flake8-html
```

## How to Run

Start the main program:
```bash
python main.py
```

You will see:
- A pre-menu (Create / Load / Exit)
- The main tournament menu after creation/loading
- Submenus for managing players and rounds

All tournament data is saved in the `/saves` folder as `.json` files.

## Project Structure

```
project/
├── main.py
├── controllers/
│   └── tournament_controller.py
├── models/
│   ├── player.py
│   ├── match.py
│   ├── round.py
│   └── tournament.py
├── views/
│   └── menu_view.py
├── saves/
├── requirements.txt
├── README.md
└── .flake8
```

## Architecture (MVC)

### Models
- `Player`: Player info and score
- `Match`: One match between two players
- `Round`: One round and its matches
- `Tournament`: The entire tournament, with logic/data

### Views
- `menu_view.py`: All menus, displays, messages, input prompts

### Controllers
- `TournamentController`: Handles user navigation, logic, saves/loads, etc.

## Saves & Loads

- Auto-save after each key action (add player, enter scores, etc.)
- Manual save (custom filename)
- Load any saved tournament from the menu
- Files in `/saves/your_tournament.json`, `/saves/autosave.json`, etc.

## Coding Conventions

- PEP8-compliant (customizable line length)
- Docstrings on all classes and methods
- Flake8 HTML report possible (see `/flake-report`)
- MVC separation: no business logic in Views, no input in Models

## Customization

- Adaptable for other sports, events, or GUI
- Easy to add new views/entities thanks to MVC structure

## Deliverables

- Complete project code
- Example save files (JSON)
- Complete README
- (Optional) Flake8 HTML code report
- (Optional) PDF/annex for presentation

## Author

Project developed for OpenClassrooms – Python Developer training  
Author: Jordan Lachaume  
Date: August 2025

## Contact / Support

Open an issue on the repo or contact me by email.
