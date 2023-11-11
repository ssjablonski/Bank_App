import unittest
from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe


class TestTransfer(unittest.TestCase):
    personal_data = {
        "name" : "Dariusz",
        "surname" : "Januszewski",
        "pesel" : "02070803628"
    }

    def test_incoming_transfer(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(pierwsze_konto.saldo, 100, "Saldo nie jest poprawne!")

    def test_incoming_transfer_with_incorrect_amount(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.zaksieguj_przelew_przychodzacy(-100)
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest poprawne!")

    def test_outgoing_transfer(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.saldo = 120
        pierwsze_konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(pierwsze_konto.saldo, 20, "Saldo nie jest poprawne!")
    
    def test_outgoing_transfer_with_incorrect_amount(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.saldo = 120
        pierwsze_konto.zaksieguj_przelew_wychodzacy(-100)
        self.assertEqual(pierwsze_konto.saldo, 120, "Saldo nie jest poprawne!")

    def test_outgoing_transfer_with_amount_greater_tan_saldo(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.saldo = 50
        pierwsze_konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(pierwsze_konto.saldo, 50, "Saldo nie jest poprawne!")

    def test_outgoing_transfer_with_promo_code(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"], "PROM_123")
        pierwsze_konto.zaksieguj_przelew_wychodzacy(20)
        self.assertEqual(pierwsze_konto.saldo, 50 - 20, "Saldo nie jest poprawne!")

    def test_series_of_transfers(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.zaksieguj_przelew_przychodzacy(100)
        pierwsze_konto.zaksieguj_przelew_przychodzacy(120)
        pierwsze_konto.zaksieguj_przelew_wychodzacy(50)
        self.assertEqual(pierwsze_konto.saldo, 100+120-50, "Saldo nie jest poprawne!")

    def test_express_acount(self):
        pierwsze_konto = Konto()
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest poprawne")

    def test_express_personal_acount(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.saldo = 100
        pierwsze_konto.zaksieguj_przelew_ekspresowy(50)
        self.assertEqual(pierwsze_konto.saldo, 100-50-1, "Saldo nie jest poprawne")

    
    def test_express_firm_acount(self):
        pierwsze_konto = KontoFirmowe("firma", "1234567890")
        pierwsze_konto.saldo = 100
        pierwsze_konto.zaksieguj_przelew_ekspresowy(50)
        self.assertEqual(pierwsze_konto.saldo, 100-50-5, "Saldo nie jest poprawne")





    