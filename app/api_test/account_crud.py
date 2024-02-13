import requests
import unittest

class TestAccountCrud(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:5000/api/accounts'

    def test_create_account(self):
        response = requests.post(self.url, json={
            "imie": "Jan",
            "nazwisko": "Kowalski",
            "pesel": "12345678900"
        })
        self.assertEqual(response.status_code, 201,"Konto nie zostało stworzone")

    def test_count_accounts(self):
        response = requests.get(self.url + "/count")
        self.assertEqual(response.status_code, 200, "Nie udało się pobrać liczby kont")

    def test_get_account_by_pesel(self):
        response = requests.get(self.url + "/12345678900")
        self.assertEqual(response.status_code, 200, "Nie udało się pobrać konta")

    def test_update_account_by_pesel(self):
        response = requests.patch(self.url + "/update/12345678900", json={
            "imie": "Janek"
        })
        self.assertEqual(response.status_code, 200, "Nie udało się zaktualizować konta")

    def test_delete_account_by_pesel(self):
        nowy = requests.post(self.url, json={
            "imie": "Jan",
            "nazwisko": "Kowalski",
            "pesel": "12345678911"
        })
        response = requests.delete(self.url + "/delete/12345678911")
        self.assertEqual(response.status_code, 200, "Konto nie zostało usunięte")