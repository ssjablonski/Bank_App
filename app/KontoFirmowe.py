from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, NIP):
        self.nazwa_firmy = nazwa_firmy
        self.NIP = NIP
        self.saldo = 0
        self.historia = []
        self.zgoda_na_kredyt = False
        if len(NIP) != 10:
            self.NIP = "Niepoprawny NIP!"
            
        else:
            self.NIP = NIP
            self.oplata_za_przelew_ekspresowy = 5
    

    def zaciagnij_kredyt(self, kwota):
        if self.saldo >= kwota*2 and -1775 in self.historia:
            self.saldo += kwota
            self.zgoda_na_kredyt = True
            return True
        else:
            return False





