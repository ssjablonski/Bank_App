import unittest

from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch

@patch("requests.get")
class TestCreateBankCompanyAccount(unittest.TestCase):
    nazwafirmy = "Biedronka"
    NIP = "8461627563"

    def test_creating_account(self, mock_request_get):
        mock_request_get.return_value.status_code = 200
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        self.assertEqual(konto.nazwa_firmy, "Biedronka", "Nazwa firmy nie została zapisana!")
        self.assertEqual(konto.NIP, "8461627563", "NIP nie został zapisany!")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_creating_account_with_incorrect_NIP(self, mock_request_get):
        mock_request_get.return_value.status_code = 404
        konto = KontoFirmowe(self.nazwafirmy, "84616275631")
        self.assertEqual(konto.nazwa_firmy, "Biedronka", "Nazwa firmy nie została zapisana!")
        self.assertEqual(konto.NIP, "Niepoprawny NIP!", "NIP nie został zapisany!")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")
    
    def test_incoming_transfer(self, mock_request_get):
        mock_request_get.return_value.status_code = 200
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto.saldo, 100, "Saldo nie jest poprawne!")

    def test_outgoing_transfer(self, mock_request_get):
        mock_request_get.return_value.status_code = 200
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 120
        konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 20, "Saldo nie jest poprawne!")
    
    def test_outgoing_transfer_with_incorrect_amount(self, mock_request_get):
        mock_request_get.return_value.status_code = 200
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 120
        konto.zaksieguj_przelew_wychodzacy(-100)
        self.assertEqual(konto.saldo, 120, "Saldo nie jest poprawne!")

    
    