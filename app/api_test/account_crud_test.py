import requests
import unittest

class TestAccountCrud(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:5000/api/accounts'
        self.konto = requests.post(self.url, json={
            "imie": "Jan",
            "nazwisko": "Kowalski",
            "pesel": "12345678900"
        })


    def test_create_account(self):
        self.assertEqual(self.konto.status_code, 201,"Konto nie zostało stworzone")

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

    def test_same_pesel(self):
        response2 = requests.post(self.url, json={
            "imie": "Jane",
            "nazwisko": "Kowalski1",
            "pesel": "12345678900"
        })
        self.assertEqual(response2.status_code, 409, "Istnieje konto o tym peselu a nowe zostalo stworzone mimo to!")
        # W TESTACH MUSISZ SZUKAC KONTO PO PESEL ZEBY MIEC DOSTEP DO SALDO!
    def test_incomig_transfer(self):
        response = requests.post(self.url + "/12345678900/transfer", json={
            "amount": 200,
            "type": "incoming"
        })
        find = requests.get(self.url + "/12345678900")
        find_json = find.json()
        self.assertEqual(find_json["Saldo"], 200, "Saldo sie nie zgadza")

    def test_outgoing_transfer(self):
        requests.post(self.url + "/12345678900/transfer", json={
            "amount": 300,
            "type": "incoming"
        })
        requests.post(self.url + "/12345678900/transfer", json={
            "amount": 200,
            "type": "outgoing"
        })
        find = requests.get(self.url + "/12345678900")
        find_json = find.json()
        self.assertEqual(find_json["Saldo"], 100, "Saldo sie nie zgadza")

    def test_outgoing_transfer_more_than_balance(self):
        requests.post(self.url + "/12345678900/transfer", json={
            "amount": 300,
            "type": "incoming"
        })
        response = requests.post(self.url + "/12345678900/transfer", json={
            "amount": 2000,
            "type": "outgoing"
        })
        find = requests.get(self.url + "/12345678900")
        find_json = find.json()
        self.assertEqual(find_json["Saldo"], 300, "Udało się wykonać przelew mimo braku środków")

    def test_incoming_transfer_wrong_pesel(self):
        response = requests.post(self.url + "/11111111111/transfer", json={
            "amount": 200,
            "type": "incoming"
        })
        self.assertEqual(response.status_code, 404, "Udało się wykonać przelew mimo zlego peselu")

    def tearDown(self):
        requests.delete(self.url + "/delete/12345678900")