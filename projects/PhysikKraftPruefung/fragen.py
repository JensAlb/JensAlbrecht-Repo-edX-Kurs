class Fragen:
    #constructor
    def __init__(self,nummer,level):
        self.nummer = nummer
        self.beschreibung = None
        self.level = level

    def set_beschreibung(self, frage_beschreibung):
        self.beschreibung = frage_beschreibung

    def get_punkte(self):
        return self.beschreibung
