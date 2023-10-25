import unittest

from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):
    nazwafirmy = "Biedronka"
    NIP = "1234567890"

    def test_creating_account(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        self.assertEqual(konto.nazwa_firmy, "Biedronka", "Nazwa firmy nie została zapisana!")
        self.assertEqual(konto.NIP, "1234567890", "NIP nie został zapisany!")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_creating_account_with_incorrect_NIP(self):
        konto = KontoFirmowe(self.nazwafirmy, "12345678901")
        self.assertEqual(konto.nazwa_firmy, "Biedronka", "Nazwa firmy nie została zapisana!")
        self.assertEqual(konto.NIP, "Niepoprawny NIP!", "NIP nie został zapisany!")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")
    
    def test_incoming_transfer(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto.saldo, 100, "Saldo nie jest poprawne!")

    def test_outgoing_transfer(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 120
        konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 20, "Saldo nie jest poprawne!")
    
    def test_outgoing_transfer_with_incorrect_amount(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 120
        konto.zaksieguj_przelew_wychodzacy(-100)
        self.assertEqual(konto.saldo, 120, "Saldo nie jest poprawne!")

    
    