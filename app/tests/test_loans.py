import unittest
from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe

class TestLoans(unittest.TestCase):
    personal_data = {
        "name" : "Dariusz",
        "surname" : "Januszewski",
        "pesel" : "02070803628"
    }

    def test_last_3_transactions(self):
        konto=KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.historia = [100, 100, 100]
        konto.zaciagnij_kredyt(250)
        self.assertEqual(konto.zgoda_na_kredyt, True, "Zgoda powinna zostać udzielona")

    def test_last_3_transactions_not_incoming(self):
        konto=KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.historia = [-100, 100, 100]
        konto.zaciagnij_kredyt(250)
        self.assertEqual(konto.zgoda_na_kredyt, False, "Ostatnie 3 tranzakcje nie sa wplatami")    

    def test_last_3_transactions_not_3(self):
        konto=KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.historia = [100, 100]
        konto.zaciagnij_kredyt(250)
        self.assertEqual(konto.zgoda_na_kredyt, False, "Ostatnie 3 tranzakcje nie sa wplatami")    


    def test_sum_5_transactions(self):
        konto=KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.historia = [100, -100, 500, -1, -10]
        konto.zaciagnij_kredyt(300)
        self.assertEqual(konto.zgoda_na_kredyt, True, "Zgoda powinna zostać udzielona")

    def test_sum_5_transactions_failed(self):
        konto=KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.historia = [-100, -100, 100, -1, -10]
        konto.zaciagnij_kredyt(300)
        self.assertEqual(konto.zgoda_na_kredyt, False, "Zgoda nie powinna zostać udzielona")

    def test_sum_5_transactions_to_small_history(self):
        konto=KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.historia = [100, -100, 500, -1]
        konto.zaciagnij_kredyt(300)
        self.assertEqual(konto.zgoda_na_kredyt, False, "Historia konta jest za krótka!")

    