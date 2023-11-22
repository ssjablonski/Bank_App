from .Konto import Konto

class RejestrKont():
    lista = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista.append(konto)

    @classmethod
    def ile_kont(cls):
        return len(cls.lista)
    
    @classmethod
    def znajdz_konto(cls, pesel):
        for konto in cls.lista:
            if konto.pesel == pesel:
                return konto
        return None