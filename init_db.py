import os
from config import DB_PATH
from data_access.database import create_tables, get_connection


def voeg_voorbeelddata_toe():
    games = [
        ("League of Legends", "MOBA"),
        ("Fortnite", "Battle Royale"), 
    ]
    
    sessies = [
         (1, "2026-11-18", 45, 1),
         (1, "2026-11-19", 38, 0),
         (2, "2026-11-19", 22, 0),
         (2, "2026-11-20", 33, 1),
         (1, "2026-11-21", 50, 1),
    ]
    with get_connection() as conn:
        for game in games:
            conn.execute("INSERT INTO games (naam, genre) VALUES (?, ?)", game)
        for sessie in sessies:
            conn.execute(
                "INSERT INTO sessies (game_id, datum, minuten, gewonnen) "
                "VALUES (?, ?, ?, ?)",
                sessie,
            )
                
def main():
    if os.path.exists(DB_PATH):
        print(f"De database bestaat al {DB_PATH}")
        return
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    create_tables()
    voeg_voorbeelddata_toe()
    print(f"Database aangemaakt: {DB_PATH}")
    
if __name__ == "__main__":
    main()
    