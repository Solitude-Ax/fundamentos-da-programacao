# Como você pode ver aqui, e esta sera uma verdade pra todas
# as próxmas estrutras, de certa forma, a gente usa a Lista Encadeada
# pra construir a Pilha, modificando suas funções para de fato
# se comportar como uma Pilha

class Stack_Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)

class Stack():
    def __init__(self, maximum_size = 255, top_node:Stack_Node = None):

        self.top = top_node
        self.maximum_size = maximum_size
        self.number_elements = 0
                
    def show_stack(self):
        
        print("\nPilha: [", end="")
        
        temp_node = self.top

        while temp_node:

            print(temp_node, end = ", ")
            temp_node = temp_node.next

        print("\b\b]\n")
        
        return
        
    def add_stack(self, value):
        
        # Esse código em especifico usa um límite de elementos, mas tirando isso,
        # É exatamente igual a função de quase mesmo nome da Lista Encadeada

        if self.maximum_size > self.number_elements:        
            
            new_node = Stack_Node(value)
            new_node.next = self.top
            self.top = new_node
            self.number_elements += 1

            print(f"Node de valor {new_node.data} adicionado a pilha")

            return
            
        else:
            
            print("\nA pilha está cheia")

            return

    def get_top(self):

        return self.top    
    
    def pop_stack(self):

        # Essa operação é igualmente inversa a função de adicionar itens,
        # e apesar de ser meio confuso o uso de "next", pensa em next aqui
        # como pegando próxmio item abaixo, e não necessáriamente a esquerda ou direita
        
        if self.number_elements > 0:

            removed_node = self.top
            self.top = self.top.next

            print(f"Node de valor {removed_node.data} retirado da pilha")

            return removed_node.data
        
        else:
            print("\nA pilha está vázia")


pilha = Stack(12)

pilha.add_stack(1)
pilha.add_stack(5)
pilha.add_stack(327)

pilha.show_stack()

pilha.pop_stack()

pilha.show_stack()

pilha.add_stack(27)

pilha.show_stack()

pilha.pop_stack()
pilha.pop_stack()

pilha.show_stack()

pilha.add_stack(84)
pilha.add_stack(55)
pilha.add_stack(18)
pilha.add_stack(97)

pilha.show_stack()

pilha.pop_stack()
pilha.pop_stack()

pilha.show_stack()