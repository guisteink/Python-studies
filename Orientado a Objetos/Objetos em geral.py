class ContaCorrente:
    contador = 123

    def __init__(self, limite, saldo):
        self._numero = ContaCorrente.contador + 1
        self._limite = limite
        self._saldo = saldo
        ContaCorrente.contador = self._numero

    def show(self):
        print(f'\nO número da sua conta é {ContaCorrente.contador}\nLimite:{self._limite}\nSaldo:{self._saldo} ')


newconta = ContaCorrente(3000, 2000)
newconta.show()