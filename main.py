from data_access.database import get_games, get_sessies


def main():
    print("Welkom bij Game Tracker!")

    print("\nGames:")
    for game in get_games():
        print(game)

    print("\nSessies:")
    for sessie in get_sessies():
        print(sessie)


if __name__ == "__main__":
    main()