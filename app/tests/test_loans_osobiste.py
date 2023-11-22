import unittest
from parameterized import parameterized
from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste


class TestLoans(unittest.TestCase):
    personal_data = {
        "name" : "Dariusz",
        "surname" : "Januszewski",
        "pesel" : "02070803628"
    }
    @parameterized.expand([
        ([100,100,100], 250, True),
        ([-100,100,100], 250, False),
        ([100,100], 250, False),
        ([100, -100, 500, -1, -10], 300, True),
        ([100, -100, 100, -1, -10], 300, False),
        ([100, -100, 500, -1], 300, False)
    ])
    def test_loan_personal(self, historia, kwota_kredytu, oczekwiany_wynik):
        konto=KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.historia = historia
        konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertEqual(konto.zgoda_na_kredyt, oczekwiany_wynik, "Zgoda powinna zostać udzielona")
