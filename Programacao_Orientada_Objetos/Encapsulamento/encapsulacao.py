# Encapsulação é o ato de deixar algo "protegido". No nosso caso,
# encapsulação é usado pra "proteger" variaveis que NÂO DEVEM ser
# modificadas* (diretamente)

# Técnicamente, a gente quer que essas variaveis sejam apenas modificadas
# internamente pela classe, por exemplo, ao invés de a gente ter um código como:
#
# nome = Antônio
#
# A gente teria uma função como essa:
#
# set_nome(self, nome)
#   self.nome = nome
#
# Isso faz com que o código seja muito mais seguro
# Claro que em um código pequeno como esse não faz diferença, mas em projetos maiores... 

class ContaBancaria:

    def __init__(self, nome, id):

        # Não existe encapsulamento em Python e um workaround pra resolver
        # isso é colocando _ ou __ antes do nome da variavel, pra indicar
        # pra outros programadores que não é pra mexer naquela variavel
        # No Java porém, a gente tem a keyword private (entre outras), que
        # segue diretamente o principio do encapsulamento

        self.__nome = nome
        self.__id = id
        self.__dinheiro = 0
        self.__investimentos = 0

    def depositar(self, deposito):
        if deposito > 0:
            self.__dinheiro += deposito
            print(f"Saldo após depósito: {self.__dinheiro}")
        else:
            print("Valor insuficiente para depósito")

    def sacar(self, saque):
        if self.__dinheiro >= saque:
            self.__dinheiro -= saque
            print(f"Saldo após saque: {self.__dinheiro}")
        else:
            print("Saldo insuficiente")

    def investir(self, investimento_comprados):
        preco = investimento_comprados * 15
        if self.__dinheiro >= preco:
            self.__dinheiro -= preco
            self.__investimentos += investimento_comprados
            print(f"Investimentos: {self.__investimentos}\nSaldo após investimento: {self.__dinheiro}")
        else:
            print("Dinheiro insuficiente para investir")

    def mostrar_saldo(self):
        print(f"Saldo: {self.__dinheiro}")

if __name__ == "__main__":
    zezinho = ContaBancaria("Zézinho", 0)

    zezinho.depositar(435)
    zezinho.sacar(138)
    zezinho.investir(10)
    zezinho.mostrar_saldo()