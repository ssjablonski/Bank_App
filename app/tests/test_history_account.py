import unittest
from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe


class TestHistory(unittest.TestCase):
    personal_data = {
        "name" : "Dariusz",
        "surname" : "Januszewski",
        "pesel" : "02070803628"
    }

    def test_history_personal_acount(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(pierwsze_konto.historia, [100], "Historia nie jest poprawna")

    def test_history_personal_account_express(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.saldo = 200
        pierwsze_konto.zaksieguj_przelew_ekspresowy(100)
        self.assertEqual(pierwsze_konto.historia, [-100, -1], "Historia nie jest poprawna")

    def test_history_personal_account_series_of_transfers(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.saldo = 200
        pierwsze_konto.zaksieguj_przelew_przychodzacy(100)
        pierwsze_konto.zaksieguj_przelew_ekspresowy(120)
        pierwsze_konto.zaksieguj_przelew_wychodzacy(2)
        pierwsze_konto.zaksieguj_przelew_przychodzacy(50)
        self.assertEqual(pierwsze_konto.historia, [100,-120,-1,-2,50], "Historia nie jest poprawna")

    def test_history_firm_acount(self):
        pierwsze_konto = KontoFirmowe("firma", "1234567890")
        pierwsze_konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(pierwsze_konto.historia, [100], "Historia nie jest poprawna")

    def test_history_firm_account_express(self):
        pierwsze_konto = KontoFirmowe("firma", "1234567890")
        pierwsze_konto.saldo = 200
        pierwsze_konto.zaksieguj_przelew_ekspresowy(100)
        self.assertEqual(pierwsze_konto.historia, [-100, -5], "Historia nie jest poprawna")

    def test_history_firm_account_series_of_transfers(self):
        pierwsze_konto = KontoFirmowe("firma", "1234567890")
        pierwsze_konto.saldo = 200
        pierwsze_konto.zaksieguj_przelew_przychodzacy(100)
        pierwsze_konto.zaksieguj_przelew_ekspresowy(120)
        pierwsze_konto.zaksieguj_przelew_wychodzacy(2)
        pierwsze_konto.zaksieguj_przelew_przychodzacy(50)
        self.assertEqual(pierwsze_konto.historia, [100,-120,-5,-2,50], "Historia nie jest poprawna")