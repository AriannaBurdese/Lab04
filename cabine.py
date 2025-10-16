class Cabina:
    def __init__(self, codice, numeroLetti, ponte, prezzo, tipologia = None):
        self.codice = codice
        self.numeroLetti = int(numeroLetti)
        self.ponte = ponte
        self.prezzo = float(prezzo)
        self.tipologia = tipologia

    def __str__(self):
        return f"{self.codice}: {self.tipologia} | {self.numeroLetti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f}€"

