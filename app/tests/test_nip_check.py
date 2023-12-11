import unittest

from unittest.mock import patch
from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe
from io import StringIO

@patch("sys.stdout", new_callable=StringIO)
@patch("requests.get")
class TestNipCheck(unittest.TestCase):
    personal_data = {
        "name" : "Firma",
        "nip" : "8461627563"
    }

    def test_correct_nip_validation(self, mock_request_get, mock_stdout):
        mock_request_get.return_value.status_code = 200
        konto=KontoFirmowe(self.personal_data["name"], self.personal_data["nip"])
        self.assertEqual(konto.nip_check(self.personal_data["nip"]), True, "NIP niepoprawny")

    def test_wrong_nip_validation(self, mock_request_get, mock_stdout):
        mock_request_get.return_value.status_code = 404
        with self.assertRaises(Exception) as context:
            konto=KontoFirmowe(self.personal_data["name"], "1234567890")
        self.assertTrue("NIP not in gov database" in str(context.exception))

    def test_wrong_nip_length(self, mock_request_get, mock_stdout):
        konto=KontoFirmowe(self.personal_data["name"], "000000000")
        self.assertEqual(konto.NIP, "Niepoprawny NIP!", "NIP powinien być niepoprawny")
        
    
