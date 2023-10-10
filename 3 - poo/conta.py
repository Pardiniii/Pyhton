class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Criando objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def mostra_saldo(self):
        print("O saldo de {} é de {} reais".format(
            self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
        print("Saldo final: {} reais.".format(self.__saldo))

    def __pode_sacar(self, valor_saque):
        return valor_saque <= self.__saldo + self.__limite

    def saca(self, valor):
        if self.__pode_sacar:
            self.__saldo -= valor
            print("Saldo final: {} reais.".format(self.__saldo))
        else:
            print("Saldo insuficiente para realizar esta transacao")

    def transfere(self, origem, destino, valor):
        origem.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def set_limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
