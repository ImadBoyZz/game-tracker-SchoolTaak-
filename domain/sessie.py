class Sessie:
    def __init__(self, game_id, datum, minuten, gewonnen, id=None):
        self.game_id = game_id
        self.datum = datum
        self.minuten = minuten
        self.gewonnen = gewonnen
        self.id = id
        
    def __str__(self):
        if self.gewonnen:
            resultaat = "gewonnen"
        else:
            resultaat = "verloren"
        return f"{self.datum} - {self.minuten} min - {resultaat}"


if __name__ == "__main__":
    s1 = Sessie(1, "2026-11-21", 45, True)
    s2 = Sessie(2, "2026-11-22", 38, False)
    print(s1)
    print(s2)