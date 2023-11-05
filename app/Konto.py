class Konto:
    
    def __init__(self):
        self.saldo = 0
        self.oplata_za_przelew_ekspresowy = 1
        
    def zaksieguj_przelew_przychodzacy(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            self.historia.append(kwota)

    def zaksieguj_przelew_wychodzacy(self, kwota):
        if kwota > 0 and kwota <= self.saldo:
            self.saldo -= kwota
            self.historia.append(-kwota)

    def zaksieguj_przelew_ekspresowy(self, kwota):
            if kwota > 0 and kwota <= self.saldo:
                self.saldo -= kwota
                self.saldo -= self.oplata_za_przelew_ekspresowy
                self.historia.append(-kwota)
                self.historia.append(-self.oplata_za_przelew_ekspresowy)







