class Queue_Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class Queue():
    def __init__(self, maximum_size = 255, head:Queue_Node = None) -> None:
        
        self.head = head
        self.tail = head
        self.maximum_size = maximum_size
        self.number_elements = 0
                
    def show_queue(self):
        
        if self.number_elements > 0:
            print("\nFila: [", end="")
            
            temp_node = self.head

            while temp_node:

                print(temp_node, end = ", ")
                temp_node = temp_node.next

            print("\b\b]\n")
        
        else:
            print("A fila está vazia")
        
        return
            
    def add_queue(self, value):
        
        # A Fila é bastante parecida com a lista encadeada na hora de 
        # adicionar itens, fazendo uso das mesmas variaveis head e tail,
        # porém, adicionando no tail ao invés do head.

        if self.maximum_size > self.number_elements:        
            
            new_node = Queue_Node(value)

            if self.tail:
                self.tail.next = new_node
                self.tail = new_node
            else:
                self.head = new_node
                self.tail = new_node
            self.number_elements += 1

            return
            
        else:
            print(f"Tentou colocar node de valor {value} mas a fila está cheia")
            return
        
    def pop_queue(self):
        
        # Head aqui, é reservado pros valores que tão no ínicio da fila 
        # e que tão prestes a sair.

        if self.number_elements > 0:

            removed_node = self.head
            self.head = self.head.next
            self.number_elements -= 1

            print(f"Node de valor {removed_node.data} retirado da fila")
        
        else:
            print("A fila está vázia")

if __name__ == "__main__":

    fila = Queue(4)

    fila.pop_queue()

    fila.add_queue(25)
    fila.add_queue(58)
    fila.add_queue(3)

    fila.show_queue()

    fila.add_queue(86)
    fila.add_queue(44)

    fila.show_queue()

    fila.pop_queue()
    fila.pop_queue()

    fila.add_queue(883)

    fila.show_queue()

    fila.pop_queue()
    fila.pop_queue()

    fila.show_queue()

    # <- [25, 58, 3, 86] <-

    # <- [58, 3, 86] <-

    # <- [58, 3, 86, 883] <-

    # <- [3, 86, 883] <-