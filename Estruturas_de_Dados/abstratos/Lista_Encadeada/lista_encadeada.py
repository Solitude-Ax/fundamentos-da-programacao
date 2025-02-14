# A Lista Encadeada é uma lista em que cada item ta
# interligado com o próximo, e isso faz que seja perfeito 
# o uso de nodes, contanto que cada node tenha uma conexão 
# com o próximo

class Node():
    def __init__(self, value):
        
        self.value = value
        self.next = None

class Linked_List():
    def __init__(self, head:Node = None):
        
        # Aqui, a gente inicia duas variáveis, head e tail, 
        # que são respectivamente o ínicio e fim da lista. 
        # Como a lista quando iniciada só tem 1 elemento, ambas 
        # as varíaveis apontam pro mesmo Node

        self.head = head
        self.tail = head
    
    def search_node(self, node):

        # Essa função, recebe o parametro do dado do Node que ta 
        # procurando, e procura pela lista por esse node. 
        # Mas o que diferencia essa função de um simples for loop, 
        # é que a gente utiliza a variavel next do node pra achar 
        # o próximo item

        # O código começa pegando o primeiro item da lista (head), 
        # e colocando numa variável como current(atual).
        # Com o While loop a gente vai indo de Node e Node, transformando 
        # current no próximo Node (current.next), enquanto current não
        # for uma varíavel vazia

        # Curiosidade: a função index do Python pra arrays funciona
        # da mesma forma, ou quase. O único porém, é que ambos os códigos
        # retornam o *primeiro* node com o dado informado

        current = self.head

        while current != None:
            if current.value == node:
                return
            
            current = current.next

    def add_node(self, value):
    
        # Essa funcção primeiramente cria um novo node com o valor
        # que você deu

        new_node = Node(value)
    
        # Se a lista não tiver vázia (head == None(Nada)), então
        # o novo node é colocado como o próximo node do node tail,
        # e depois o nosso novo node se torna o tail

        if self.head != None:
            self.tail.next = new_node
            self.tail = self.tail.next
            self.print_list()
        
        # Se não a gente bota o novo node como tanto o head quanto o tail

        else:
            self.head = new_node
            self.tail = self.head
            self.print_list()
    
    def test_add_nodes(self, array):
        
        print(f"Adicionando os valores {array}")
        
        for value in array:
            self.add_node(value)
    
    def remove_node(self, value):

        # Em primeiro lugar, se a lsita tiver vazia, o código
        # printa "a lista ta vazia"
        
        if not self.head:
            print("A lista ta vazia")
            return
        
        # Essa função utiliza um pouco da mesma lógica da
        # função de achar um node, e muitas outras estruturas vão 
        # usar a mesma lógica, então não vou fica me repetindo muito
        
        # Aqui, o código é exatamente igual a função de procurar

        current = self.head
        #print(current.next.value)
        
        if self.head.value == value:
            self.head = self.head.next
        
        else:
            
            while current.next != None:

                # Porém aqui, ao invés de só printar o valor ou 
                # retornar, a função utiliza da variavel next

                # Explicando melhor, essa função itera pela lista,
                # e se o valor do próxmo node do node atual 
                # (como node(27) -> node(5)) for o dado a ser removido,
                # a função faz uma "cirurgia", essencialmente fazendo isso aqui:
                # 1 | node(27) -> node(5) -> Node(13) |
                # 2 | node(27) -> Node(13) |

                if current.next.value == value:
                        current.next = current.next.next
                        self.print_list()
                        return
                
                current = current.next
            
            print(f"O valor {value} não existe na lista")
            self.print_list()
    
    def print_list(self):
        
        if self.head:
            current = self.head
            
            while current != None:
                print(current.value, end=" -> " if current.next else " -> None\n")
                current = current.next
                
        else:
            print("lista ta vaziazinha\n")

listanho = Linked_List()
listanho.test_add_nodes([25, 4, 28, 36, 44, 55, 6])
listanho.remove_node(6)
listanho.remove_node(25)
listanho.remove_node(4)
listanho.remove_node(825)
listanho.remove_node(36)