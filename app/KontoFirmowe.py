from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, NIP):
        self.nazwa_firmy = nazwa_firmy
        self.NIP = NIP
        self.saldo = 0

        if len(NIP) != 10:
            self.NIP = "Niepoprawny NIP!"
        else:
            self.NIP = NIP






