from datetime import datetime
import unittest
from unittest.mock import patch, MagicMock

from ..SMTPConnection import SMTPConnection
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe


class TestSendHistoryOnMail(unittest.TestCase):
    personal_data = {
        "name" : "Dariusz",
        "surname" : "Januszewski",
        "pesel" : "02070803628"
    }

    firm_data = {
        "name" : "Firma",
        "nip" : "8461627563"
    }

    def test_check_if_method_was_called(self):
        smtp_connection = SMTPConnection()
        smtp_connection.wyslij = MagicMock()
        smtp_connection.wyslij("Temat", "Tresc", "Adresat")
        smtp_connection.wyslij.assert_called_once_with("Temat", "Tresc", "Adresat")

    def test_check_true(self):
        smtp_connection = SMTPConnection()
        smtp_connection.wyslij = MagicMock(return_value=True)
        self.assertEqual(smtp_connection.wyslij("Temat", "Tresc", "Adresat"), True, "Wysyłanie powinno się powieść")

    def test_check_false(self):
        smtp_connection = SMTPConnection()
        smtp_connection.wyslij = MagicMock(return_value=False)
        self.assertEqual(smtp_connection.wyslij("Temat", "Tresc", "Adresat"), False, "Wysyłanie powinno się nie powieść")

    def test_check_personal(self):
        konto=KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.saldo = 100
        konto.zaksieguj_przelew_wychodzacy(50)
        smtp_connection = SMTPConnection()
        smtp_connection.wyslij = MagicMock(return_value=True)
        status = konto.wyslij_historie_na_maila("Adresat", smtp_connection)
        self.assertTrue(status)
        smtp_connection.wyslij.assert_called_once_with(f"Wyciąg z dnia {datetime.today().strftime('%Y-%m-%d')}", f"Twoja historia konta to: {konto.historia}", "Adresat")

    @patch('app.KontoFirmowe.KontoFirmowe.nip_check')
    def test_check_firm(self, nip_check):
        nip_check.return_value = True
        konto=KontoFirmowe(self.firm_data["name"], self.firm_data["nip"])
        konto.saldo = 100
        konto.zaksieguj_przelew_wychodzacy(50)
        smtp_connection = SMTPConnection()
        smtp_connection.wyslij = MagicMock(return_value=True)
        status = konto.wyslij_historie_na_maila("Adresat", smtp_connection)
        self.assertTrue(status)
        smtp_connection.wyslij.assert_called_once_with(f"Wyciąg z dnia {datetime.today().strftime('%Y-%m-%d')}", f"Historia konta Twojej firmy to: {konto.historia}", "Adresat")

    