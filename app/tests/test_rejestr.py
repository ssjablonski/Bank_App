import unittest

from ..RejestrKont import RejestrKont
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe

class TestRejestr(unittest.TestCase):
    imie="darek"
    nazwisko="kowalski"
    pesel="12345678900"

    @classmethod
    def setUpClass(cls):
        cls.konto = KontoOsobiste(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.dodaj_konto(cls.konto)

    def test_dodaj_konto(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto2 = KontoOsobiste(self.imie + "d", self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        RejestrKont.dodaj_konto(konto2)
        self.assertEqual(RejestrKont.ile_kont(), 3, "Niepoprawna ilosc kont")

    def test_znajdz_konto(self):
        konto = RejestrKont.znajdz_konto(self.pesel)
        self.assertEqual(konto, self.konto, "Nie znaleziono konta")

    def test_znajdz_konto_zly_pesel(self):
        konto = RejestrKont.znajdz_konto("12345678911")
        self.assertEqual(konto, None, "Znaleziono konto ktorego nie ma")

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []