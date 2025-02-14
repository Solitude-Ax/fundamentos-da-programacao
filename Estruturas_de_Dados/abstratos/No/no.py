# Essa é a estrutura de dados mais básica que tem

# Como você pode ver, ela tem 2 variaveis: 
# uma variavel de dado, e a outra do próximo node na "lista"

class Node():
    def __init__(self, data):
        
        self.data = data
        self.next = None

no_1 = Node(3)
no_2 = Node(27)

# Aqui, o no_2 ta sendo colocado como o próximo node depois de no_1

no_1.next = no_2

# O código abaixo da erro, no_2 não tem próximo (next)

print(no_1.data)
print(no_1.next.data)
print(no_2.next.data)