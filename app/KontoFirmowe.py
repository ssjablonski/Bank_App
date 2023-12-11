from datetime import date
from .Konto import Konto
import requests
import os

load_dotenv()

class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, NIP):
        self.nazwa_firmy = nazwa_firmy
        self.NIP = NIP
        self.saldo = 0
        self.historia = []
        self.zgoda_na_kredyt = False
        if len(NIP) == 10:
            if self.nip_check(NIP):
                self.NIP = NIP
                self.oplata_za_przelew_ekspresowy = 5
            else:
                raise Exception("NIP not in gov database")
        else:
            self.NIP = "Niepoprawny NIP!"
        
    

    def zaciagnij_kredyt(self, kwota):
        if self.saldo >= kwota*2 and -1775 in self.historia:
            self.saldo += kwota
            self.zgoda_na_kredyt = True
            return True
        else:
            return False
        
    def nip_check(self, nip):
        url = os.getenv("BANK_APP_MF_URL", 'https://wl-test.mf.gov.pl/api/search/nip/')
        data = date.strftime(date.today(), "%Y-%m-%d")
        response = requests.get(url + "api/search/nip/" + nip + "?date=" + data)
        # print(response.status_code, response.json())
        if response.status_code == 200:
            print(True)
            return True
        print(False)
        return False