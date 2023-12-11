import unittest
from parameterized import parameterized
from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch

class TestLoans(unittest.TestCase):
    personal_data = {
        "name" : "Firma",
        "nip" : "8461627563"
    }

    @parameterized.expand([
            # historia, kwota kredytu, saldo, oczekiwany kredyt
            ([100,100,100, -1775], 250, 600, True ),
            ([100,100,100, 1775], 250, 500, False ),
            ([-100,100,100,-1775], 250, 400, False),
            ([-100,100,100,1775], 250, 400, False),
        ])
    @patch("requests.get")
    def test_loan_firm(self,historia, kwota_kredytu, saldo, oczekwiany_wynik, mock_request_get):
        mock_request_get.return_value.status_code = 200
        konto=KontoFirmowe(self.personal_data["name"], self.personal_data["nip"])
        konto.historia = historia
        konto.saldo = saldo
        konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertEqual(konto.zgoda_na_kredyt, oczekwiany_wynik, "Zgoda powinna zostać udzielona")