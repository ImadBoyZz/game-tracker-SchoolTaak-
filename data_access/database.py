import sqlite3
from config import DB_PATH

def get_connection():
    """Geeft een verbinding met de database terug."""
    return sqlite3.connect(DB_PATH)

def create_tables():
    """Maakt de tabellen games en sessies aan (als ze nog niet bestaan)."""
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT NOT NULL UNIQUE,
            genre TEXT 
        )
    """)
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS sessies(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     game_id INTEGER NOT NULL,
                     datum TEXT NOT NULL,
                     minuten INTEGER NOT NULL,
                     gewonnen INTEGER NOT NULL,
                     FOREIGN KEY (game_id) REFERENCES games(id)      
        )
    """)