import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "02070803628"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie zostal napisany")
    
    def test_pesel_with_len_10(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za krótki pesel został przujęty za prawidłowy")

    def test_pesel_with_len_12(self):
        konto = Konto(self.imie, self.nazwisko, "123456789000")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za długi pesel został przujęty za prawidłowy")

    def test_empty_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za krótki pesel został przyjęty za prawidłowy")

    def test_promo_wrong_prefix(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "prom_123")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_promo_wrong_suffix(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_1233")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_promo_wrong_len(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_promo_correct(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_123")
        self.assertEqual(konto.saldo, 50, "Promocja nie została naliczona!")

    def test_birthday_pre_1960_correct_promo_valid_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "56120774938", "PROM_123")
        self.assertEqual(konto.saldo, 0,"Osoba urodzona jest przed 1960!")

    def test_birthdat_post_1960_correct_promo_valid_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "02070803628", "PROM_123")
        self.assertEqual(konto.saldo, 50, "Promocja nie została naliczona")

    def test_birthday_pre_1960_correct_promo_invalid_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "59121211111", "PROM_123")
        self.assertEqual(konto.saldo, 0,"Saldo nie jest zerowe!")

    def test_birthdat_post_1960_correct_promo_invalid_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "02111111111", "PROM_123")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_birthday_pre_1960_wrong_promo_valid_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "56120774938", "_123")
        self.assertEqual(konto.saldo, 0,"Saldo nie jest zerowe!")

    def test_birthdat_post_1960_wrong_promo_valid_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "02111111111", "_123")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_birthday_pre_1960_wrong_promo_invalid_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "59121211111", "_123")
        self.assertEqual(konto.saldo, 0,"Saldo nie jest zerowe!")

    def test_birthdat_post_1960_wrong_promo_invalid_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "02111111111", "_123")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")



    

    
    #tutaj proszę dodawać nowe testy