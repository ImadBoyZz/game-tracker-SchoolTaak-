import sqlite3
from config import DB_PATH
from domain.game import Game
from domain.sessie import Sessie


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
            CREATE TABLE IF NOT EXISTS sessies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_id INTEGER NOT NULL,
                datum TEXT NOT NULL,
                minuten INTEGER NOT NULL,
                gewonnen INTEGER NOT NULL,
                FOREIGN KEY (game_id) REFERENCES games(id)
            )
        """)


def get_games():
    """Haalt alle games op en geeft een lijst van Game-objecten terug."""
    with get_connection() as conn:
        rows = conn.execute("SELECT id, naam, genre FROM games").fetchall()
    games = []
    for row in rows:
        game = Game(row[1], row[2], row[0])
        games.append(game)
    return games


def get_sessies():
    """Haalt alle sessies op en geeft een lijst van Sessie-objecten terug."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, game_id, datum, minuten, gewonnen FROM sessies ORDER BY datum"
        ).fetchall()
    sessies = []
    for row in rows:
        gewonnen = row[4] == 1
        sessie = Sessie(row[1], row[2], row[3], gewonnen, row[0])
        sessies.append(sessie)
    return sessies


def add_sessie(sessie):
    """Voegt een nieuwe sessie toe aan de database."""
    query = """INSERT INTO sessies (game_id, datum, minuten, gewonnen)
               VALUES (?, ?, ?, ?)"""
    parameters = (sessie.game_id, sessie.datum, sessie.minuten, sessie.gewonnen)
    with get_connection() as conn:
        conn.execute(query, parameters)
        conn.commit()


def update_sessie(sessie):
    """Wijzigt een bestaande sessie (op basis van haar id)."""
    query = """UPDATE sessies
               SET game_id = ?, datum = ?, minuten = ?, gewonnen = ?
               WHERE id = ?"""
    parameters = (sessie.game_id, sessie.datum, sessie.minuten,
                  sessie.gewonnen, sessie.id)
    with get_connection() as conn:
        conn.execute(query, parameters)
        conn.commit()