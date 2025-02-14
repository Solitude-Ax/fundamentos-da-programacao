import heapq

# Sim, esse algoritmo é um pouquinho mais complicado que os outros

# Em primeiro lugar, a gente precisa de uma forma de pegar os menores valores em uma lista, e por isso
# a gente usa heapq, que em resumo, é uma árvore, onde o menor valor fica no topo

# Em seguida, a gente cria duas classes: Node e Grafo

# Node é apenas uma forma de guardar um dado, e __repr__ é uma forma de representar o node
# sem ter um aneurisma lendo <__main__.Node object at 0x000002AB26B1F390>

class Node:

    def __init__(self, data):
        
        self.data = data
    
    def __repr__(self):

        return f"{self.data}"

class Graph:

    def __init__(self):
        
        # Este dicionário, guarda os nodes com seus respectivos vertices
        # conectados, seguindo a sintaxe:
        # {node : {node_conectado: peso}}
        self.graph = {}

        # Já este dicionário, guarda os vertices para um acesso seguro e rápido,
        # fazendo com que seja possivel acessar um node com o dado que ele guarda:
        # {dado_do_node: node}
        self.vertices = {}
    
    def dijkstra(self):

        # Com este, a gente guarda as distancias, usando o Node, então se por algum motivo você quer acessar
        # a distancia mais curta de um node, você pode acessar esse dado usando esse dicionário

        distances = {}

        # O que esta sendo feito aqui é colocar todos os do gráfo no dicionário acima, com uma distancia de
        # valor infinito

        for vertex in self.graph.keys():
            distances[vertex] = float("inf")

        # Em seguida, o algoritmo pega o primeiro valor do dicionário. Não necessáriamente precisa ser o primeiro,
        # pode ser o último ou um qualquer no meio se quiser, mas pra mim é mais intuitivo
    
        current = list(self.graph.keys())[0]

        # Esse Node que o algoritmo pegou, que a gente vai chamar de Atual, então atualizado no dicionário de
        # distâncias, colocando o valor 0, porque a gente vai medir a distância desse node pra todos os outros node do gráfo,
        # e pelo fato da distancia do node Atual para o node Atual ser 0, a gente coloca 0

        # Porém, a gente também cria uma variável chamada de Q(Queue) que se traduz em Fila em português, que é como a gente
        # vai fazer pra percorrer pelo gráfo
        # (se você não sabe o que é uma fila, eu tenho outro repositório explicando Estruturas de Dados)
        #
        # Essa fila guarda tuplas de sintaxe:
        #
        # (distância_do_node_inicial, node)

        distances[current] = 0
        q = [(distances[current], current)]

        # Ignore, é pra debug
        print(distances)

        # Aqui, a gente cria um loop que vai continuar enquanto Q tiver um tamanho maior que 0
        #
        # Óbviamente, não preciso dizer que a gente precisa se certificar que esse array ta tendo
        # valores removidos

        while len(q) > 0:

            # Como a gente colocou uma tupla naquele array, a gente pode usar esse tipo de atribuição e criação de
            # sintaxe pra criar duas variáveis diferentes
            #
            # Além disso, a gente deve usar o método heappop de heapq, já que ele vai retirar o Node com a
            # menor distância na tupla
            #
            # Já a variavel current_graph é só pra facilitar pegar os Nodes conectados correto

            distance, current = heapq.heappop(q)
            current_graph = self.graph[current]

            # Aqui, agente itera pelos nodes conectados do Node Atual
            #
            # Esse segundo node a gente vai chamar de Iterado

            for connected, weight in current_graph.items():
                
                # Se a distancia do Atual mais o peso Iterado for menor que a distância do dicionário
                # de distâncias do Iterado, a gente atualiza esse dicionário pra guardar essa distância menor
                #
                # Iterado: 4, Atual: 7
                #
                # distances[Iterado] = 21
                #
                # -------------------------
                #
                # distances[Iterado] = 13

                if distance + weight < distances[connected]:

                    # E então a gente coloca esse iterado na fila

                    distances[connected] = distance + weight
                    heapq.heappush(q, (distances[connected], connected))
                
            print(distances)
            
        print(end="\n\n")
                

    # ~ - - ~ - ~ - - ~ - ~ - - ~ Ignore, funções de Gráfo ~ - - ~ - ~ - - ~ - ~ - - ~

    # Se você tiver interessado em saber o que essas funções fazem, eu tenho outro repositório explicando
    # a lógica por traz dessas funções

    def add_vertex(self, vertice_data):

        new_node = Node(vertice_data)
        self.graph[new_node] = {}
        self.vertices[vertice_data] = new_node
    
    def connect_vertices(self, source, destination, weight):

        source = self.vertices[source]
        destination = self.vertices[destination]

        self.graph[source][destination] = weight
    
    def print_graph(self):

        for vertice in self.graph.items():
            print(vertice)
        
        print(end="\nend of graph\n\n")

    # ~ - - ~ - ~ - - ~ - ~ - - ~ Ignore, funções de Gráfo ~ - - ~ - ~ - - ~ - ~ - - ~


if __name__ == "__main__":

    grafo = Graph()

    grafo.add_vertex(0)
    grafo.add_vertex(4)
    grafo.add_vertex(8)
    grafo.add_vertex(12)
    grafo.add_vertex(16)
    grafo.add_vertex(24)
    grafo.add_vertex(38)

    grafo.print_graph()

    grafo.connect_vertices(0, 4, 3)
    grafo.connect_vertices(0, 8, 9)
    grafo.connect_vertices(4, 12, 12)
    grafo.connect_vertices(8, 12, 5)
    grafo.connect_vertices(12, 24, 4)
    grafo.connect_vertices(12, 16, 15)
    grafo.connect_vertices(24, 38, 19)
    grafo.connect_vertices(16, 38, 38)

    grafo.print_graph()

    grafo.dijkstra()

    grafo.print_graph()