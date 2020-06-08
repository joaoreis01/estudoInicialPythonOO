

class Conta:
        #o __ antes do nome do atributo é referente ao modificador de acesso private
    def __init__(self, numero, titular, saldo, limite):
        print(f"Endereço de memória do objeto criado em {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print(f" Saldo do {self.__titular} é de {self.__saldo}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): #Tornando a classe privada
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar  # Se o valor_a_sacar for >= que valor_disponivel_a_sacar retorna true, senão false 

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'o valor {valor} passou o limite, saque não efetuado')


    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property #Funciona como o get, porém ele é chamado com a seguinte sintaxe conta1.numero, sem o clássico () de função
    def numero(self):
        print('chamando property numero()')
        return self.__numero

    @property
    def titular(self):
        print('chamando property titular()')
        return self.__titular

    @property
    def saldo(self):
        print('chamando property saldo()')
        return self.__saldo

    @property
    def limite(self):
        print('chamando property limite()')
        return self.__limite    

    @limite.setter #Funciona como o set, porém ele é chamado com a seguinte sintaxe conta1.limite = 1000, sem o clássico () de função e sim o '= novoLimite'
    def limite(self, novoLimite):
        print('chamando o setter limite()')
        self.__limite = novoLimite     

    @staticmethod 
    def codigo_banco():
        return '001'

    @staticmethod 
    def codigo_dos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}