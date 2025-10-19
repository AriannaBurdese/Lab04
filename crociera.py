from cabine import Cabina, CabineDeluxe, Animali
from passeggeri import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.listaPasseggeri = []
        self.listaCabine = []


    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r") as file:
                righe = file.readlines()
            for riga in righe:
                campi = riga.strip('\n').split(',')
                if len(campi) == 3:
                    passeggeri = Passeggero(campi[0], campi[1], campi[2])
                    self.listaPasseggeri.append(passeggeri)
                elif len(campi) == 4:
                    cabine = Cabina(campi[0], campi[1], campi[2], campi[3])
                    self.listaCabine.append(cabine)
                elif len(campi) == 5:
                    if campi[4].isdigit():
                        cabine = Animali(campi[0], campi[1], campi[2], campi[3], int(campi[4]))
                    else:
                        cabine = CabineDeluxe(campi[0], campi[1], campi[2], campi[3], campi[4])
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
        cabina_trovata = None
        for cabina in self.listaCabine:
            if cabina.codice == codice_cabina:
                cabina_trovata = cabina
                break
        if cabina_trovata is None:
            raise Exception("Cabina non trovata")

        passeggero_trovato = None
        for passeggero in self.listaPasseggeri:
            if passeggero.codice == codice_passeggero:
                passeggero_trovato = passeggero
                break
        if passeggero_trovato is None:
            raise Exception("Passeggero non trovato")


        if not getattr(cabina_trovata, "disponibile", True):
            raise Exception("Cabina non disponibile")

        if getattr(passeggero_trovato, "cabina", None) is not None:
            raise Exception("Passeggero già assegnato ad una cabina")

        passeggero_trovato.cabina = cabina_trovata
        cabina_trovata.disponibile = False

        print(f"Passeggero {passeggero_trovato.codice} assegnato alla cabina {cabina_trovata.codice}")



    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""

        for cabina in self.listaCabine:
            if isinstance(cabina, Animali):
                prezzo_base = cabina.prezzo
                maxAnimali = cabina.maxAnimali
                prezzo_finale = prezzo_base*(1 + 0.10* maxAnimali)
                cabina.prezzo = prezzo_finale

            if isinstance(cabina, CabineDeluxe):
                prezzo_base = cabina.prezzo
                prezzo_finale = prezzo_base* 1.20
                cabina.prezzo = prezzo_finale


        prezzo = prezzo_finale
        cabine_ordinate_per_prezzo = sorted(self.listaCabine, key = lambda x:x.prezzo)
        return cabine_ordinate_per_prezzo


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for passeggero in self.listaPasseggeri:
            cabina_associata = passeggero.cabina
            if cabina_associata is not None:
                print(f"Il passeggero {passeggero.codice} è associato alla cabina {cabina_associata.codice}")
            else:
                print(f"Passeggero {passeggero.codice} non associato")

