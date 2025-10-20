class Passeggero:
    def __init__(self, codice, nome, cognome):
        self._codice = codice
        self._nome = nome
        self._cognome = cognome
        self._cabina = None

    @property
    def codice(self):
        return self._codice
    @codice.setter
    def codice(self, valore):
        self._codice = valore
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valore):
        self._nome = valore
    @property
    def cognome(self):
        return self._cognome
    @cognome.setter
    def cognome(self, valore):
        self._cognome = valore
    @property
    def cabina(self):
        return self._cabina
    @cabina.setter
    def cabina(self, valore):
        self._cabina = valore





    def __str__(self):
        return f"{self.codice}, nome: {self.nome}, cognome: {self.cognome}"

