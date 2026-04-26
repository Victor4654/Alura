class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = str(titular).title()
        self.saldo = float(saldo)
        self._ativo = False

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: {self.saldo:.2f} | Status: {self._ativo}"
    
    @property
    def ativar_conta(self):     
        self._ativo = True




conta1 = ContaBancaria("victor teles farias", 3542.12)
conta2 = ContaBancaria("josé da conceição dos santos", 4567.48)
conta1.ativar_conta
print(conta1)
print(conta2)
        

class ContaBancariaPythonica:

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
    def ativar_conta(self):
        self._ativo = True



conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")


class ClienteBanco:

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta
    
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")