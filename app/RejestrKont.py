from .Konto import Konto
from .KontoOsobiste import KontoOsobiste
from pymongo import MongoClient


class RejestrKont():
    client = MongoClient('localhost', 27017)
    db = client['bankApp']
    collection = db['rejestr_kont']
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
    
    @classmethod
    def usun_konto(cls, pesel):
        konto = cls.znajdz_konto(pesel)
        cls.lista.remove(konto)

    @classmethod
    def load(cls):
        cls.lista = []
        for konto in cls.collection.find({}):
            # if konto["pesel"] is not None:
            acc = KontoOsobiste(konto["imie"], konto["nazwisko"], konto["pesel"])
            acc.saldo = konto["saldo"]
            acc.historia = konto["historia"]
            cls.lista.append(acc)

    @classmethod
    def save(cls):
        cls.collection.delete_many({})
        for konto in cls.lista:
            cls.collection.insert_one({"imie": konto.imie, "nazwisko": konto.nazwisko, "pesel": konto.pesel, "saldo": konto.saldo, "historia": konto.historia})