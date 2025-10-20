class Cabina:
    def __init__(self, codice, numeroLetti, ponte, prezzo, tipologia = "Standard"):
        self._codice = codice
        self._numeroLetti = int(numeroLetti)
        self._ponte = ponte
        self._prezzo = float(prezzo)
        self._tipologia = tipologia
        self._disponibile = True



    #creo i metodi getter and setter
    @property
    def codice(self):
        return self._codice
    @codice.setter
    def codice(self, valore):
        self._codice = valore

    @property
    def numeroLetti(self):
        return self._numeroLetti
    @numeroLetti.setter
    def numeroLetti(self, valore):
        if int(valore) > 0:
            self._numeroLetti = int(valore)
        else:
            raise ValueError("Il numero di letti deve essere positivo")

    @property
    def ponte(self):
        return self._ponte
    @ponte.setter
    def ponte(self, valore):
        self._ponte = valore

    @property
    def prezzo(self):
        return self._prezzo
    @prezzo.setter
    def prezzo(self, valore):
        if float(valore) > 0:
            self._prezzo = float(valore)
        else:
            raise ValueError("Il prezzo deve essere positivo")

    @property
    def tipologia(self):
        return self._tipologia
    @tipologia.setter
    def tipologia(self, valore):
        self._tipologia = valore if valore else "Standard"

    @property
    def disponibile(self):
        return self._disponibile
    @disponibile.setter
    def disponibile(self, valore):
        if not isinstance(valore, bool):
            raise ValueError(" disponibile deve essere True o False")

    def __str__(self):
        tipologia = self.tipologia if self.tipologia is not None else "Standard"
        return f"{self.codice}: {self.tipologia} | {self.numeroLetti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f} - tipologia: {self.tipologia}"


class CabineDeluxe(Cabina):
    def __init__(self, codice, numeroLetti, ponte, prezzo, serviziExtra):
        super().__init__(codice, numeroLetti, ponte, prezzo, tipologia = "Deluxe")
        self.serviziExtra = serviziExtra

    @property
    def serviziExtra(self):
        return self._serviziExtra
    @serviziExtra.setter
    def serviziExtra(self, valore):
        self._serviziExtra = valore if valore else "Standard"

    def __str__(self):
        return super().__str__() + f"-Servizio Extra: {self.serviziExtra}"

class Animali(Cabina):
    def __init__(self, codice, numeroLetti, ponte, prezzo, maxAnimali):
        super().__init__(codice, numeroLetti, ponte, prezzo, tipologia = "Animali")
        self._maxAnimali = maxAnimali

    @property
    def maxAnimali(self):
        return self._maxAnimali
    @maxAnimali.setter
    def maxAnimali(self, valore):
        if int(valore) >= 0:
            self._maxAnimali = int(valore)
        else:
            raise ValueError("Il numero massimo di animali deve essere positivo")

    def __str__(self):
        return super().__str__() + f"-Max Animali: {self.maxAnimali}"


