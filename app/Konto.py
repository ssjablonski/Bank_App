class Konto:
    def __init__(self):
        self.saldo = 0
        
    def zaksieguj_przelew_przychodzacy(self, kwota):
        if kwota > 0:
            self.saldo += kwota

    def zaksieguj_przelew_wychodzacy(self, kwota):
        if kwota > 0 and kwota <= self.saldo:
            self.saldo -= kwota



