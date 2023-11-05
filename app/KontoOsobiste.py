from .Konto import Konto

class KontoOsobiste(Konto):
    def __init__(self, imie, nazwisko, pesel, promo_code = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.historia = []

        if len(pesel) != 11:
            self.pesel = "Niepoprawny pesel!"
        else:
            self.pesel = pesel
            self.oplata_za_przelew_ekspresowy = 1

        if self.is_promo_code_correct(promo_code) and self.is_pesel_correct(pesel):
            self.saldo = 50
        else:
            self.saldo = 0

    def is_promo_code_correct(self, promo_code):
        if promo_code is None:
            return False
        if promo_code.startswith("PROM_") and len(promo_code) == 8:
            return True
        else:
            return False
        
    def is_pesel_correct(self, pesel):
        dwie = pesel[0] + pesel[1]
        if int(dwie) > 60 or int(dwie) <= 23:
            controls = "1379137913"
            licznik = 0
            for i in range(len(pesel)-1):
                licznik += (int(pesel[i])*int(controls[i])) % 10

            last_digit = 10 - (licznik%10)
            if str(last_digit) == pesel[-1]:
                return True
            else:
                return False
        else:
            return False



