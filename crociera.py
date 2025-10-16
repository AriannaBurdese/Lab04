from cabine import Cabina
from passeggeri import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.listaPasseggeri = []
        self.listaCabine = []

#creo classi con altri file
#creo altre 2 classi per cabina delux e cabina animali
#differenzio passeggeri e cabine in base al numero di campi che hanno

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r") as file:
                righe = file.readlines()
            for riga in righe:
                campi = riga.strip('\n').split(',')
                print(campi)
                if len(campi) == 3:
                    passeggeri = Passeggero(campi[0], campi[1], campi[2])
                    self.listaPasseggeri.append(passeggeri)
                elif len(campi) == 4:
                    cabine = Cabina(campi[0], campi[1], campi[2], campi[3])
                    self.listaCabine.append(cabine)
                elif len(campi) == 5:
                    cabine = Cabina(campi[0], campi[1], campi[2], campi[3], campi[4])
                    self.listaCabine.append(cabine)
                else:
                    print("Riga non valida")


            for cabina in self.listaCabine:
                print(cabina)
            for passeggero in self.listaPasseggeri:
                print(passeggero)
        except FileNotFoundError:
            print("File non trovato")















    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

