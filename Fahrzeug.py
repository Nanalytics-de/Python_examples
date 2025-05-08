# Superklasse ------------------------------------------------------------------------
class Fahrzeug:
    def Beschreibung(self):
        print("Ich bin ein Fahrzeug")

# 1. Level Unterklasse -----------------------------------------------------------------------        
class Auto(Fahrzeug):
    def __init__(self, farbe: str, maxgeschw: int, anzahlsitze: int):
        self.farbe = farbe
        self.maxgeschw = maxgeschw
        self.anzahlsitze = anzahlsitze
    def Beschreibung(self):
        print("Ich bin ein Auto")
        
class Bahn(Fahrzeug):
    def Beschreibung(self):
        print("Ich bin eine Bahn")
        
# 2. Level Unterklasse -----------------------------------------------------------------------
class Cabrio(Auto):        
    def __init__(self, farbe: str, maxgeschw: int, anzahlsitze: int, dach: str):
        super().__init__(farbe, maxgeschw, anzahlsitze)
        self.dach = dach
        
        
    def __str__(self):
        return f"Ich bin ein {self.farbe} Cabrio mit einem {self.dach} Dach, der Klasse: \t {super().__str__()}"
    
class SUV(Auto):
    def __init__(self):
        super.__init__()
        
    def __str__(self):
        return f"Ich bin ein {self.farbe} Cabrio der Klasse: \t {super().__str__()}"
        
# ----- Objekte        
a = Cabrio('rot', 120, 2, 'Leder')   
print(a)     
a.Beschreibung()
            