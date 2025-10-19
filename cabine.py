class Cabina:
    def __init__(self, codice, numeroLetti, ponte, prezzo, tipologia = "Standard"):
        self.codice = codice
        self.numeroLetti = int(numeroLetti)
        self.ponte = ponte
        self.prezzo = float(prezzo)
        self.tipologia = tipologia
        disponibile = True
    def __str__(self):
        tipologia = self.tipologia if self.tipologia is not None else "Standard"
        return f"{self.codice}: {self.tipologia} | {self.numeroLetti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f} - tipologia: {self.tipologia}"


class CabineDeluxe(Cabina):
    def __init__(self, codice, numeroLetti, ponte, prezzo, serviziExtra):
        super().__init__(codice, numeroLetti, ponte, prezzo, tipologia = "Deluxe")
        self.serviziExtra = serviziExtra

    def __str__(self):
        return super().__str__() + f"-Servizio Extra: {self.serviziExtra}"

class Animali(Cabina):
    def __init__(self, codice, numeroLetti, ponte, prezzo, maxAnimali):
        super().__init__(codice, numeroLetti, ponte, prezzo, tipologia = "Animali")
        self.maxAnimali = maxAnimali

    def __str__(self):
        return super().__str__() + f"-Max Animali: {self.maxAnimali}"


