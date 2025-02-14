# Ok, peço que tenha paciencia agora, porque esse aqui
# talvez não seja tão intuitivo quantos os outros

# A minha implementação utiliza dicionários pra 
# acessar os vértices (como nodes são chamados em gráfos) e
# uma variavel de posição pra ajudar na função de
# tirar e adicionar vétices

# Em um Gráfo de Matriz Adjacente, a gente usa 
# matrizes bidimensionais ("arrays" com altura e largura) pra
# representar as conexões entre os nodes do Grafo,
# aonde 0 significa sem conexão, e 1 significa com, por exemplo:
#
# [[0, 1, 0]] Node 1 ta conectado com Node 2
# [[1, 0, 1]] Node 2 ta conectado com Node 1 e Node 3
# [[0, 1, 0]] Node 3 ta conectado com Node 2

class Vertice:

    def __init__(self, data):
        
        # E sim, cabo a mamata das variavez next

        self.data = data
        self.position = None
    
    def __repr__(self):
        return f"{self.data}"

class Graph:

    def __init__(self):
        
        self.position_count = 0

        # Esse dicionáio é usado pra ter acesso a um node
        # usando o seu dado
        self.vertices = {}

        # O array inicial aonde a matriz vai ficar
        self.graph = []
    
    def add_vertex(self, data_vertex):

        # Essa função adiciona o Node no gráfo se o dado dele já
        # não existe no dicionário contendo todos os nossos vértices

        if data_vertex not in list(self.vertices.keys()):

            # Criando o novo Node, e adicionando ele ao dicionário de
            # vértices

            vertice = Vertice(data_vertex)

            vertice.position = self.position_count
            self.vertices[data_vertex] = vertice

            # Criando um array contendo 0s e 1s do mesmo tamanho do nosso
            # Grafo de Matriz, pra eventualmente adicionar a essa matriz

            vertex_array = [0 for _ in range(len(self.graph)+1)]

            for vertice_list in self.graph:
                vertice_list += [0 for _ in range(len(vertex_array) - len(vertice_list))]
            
            self.graph.append(vertex_array)
            self.position_count += 1
    
    def connect_vertices(self, vertice_source, vertice_destination):

        # Essa função basicamente acessa no nosso Grafo de Matriz nas posições de
        # ambos os vertices que a gente ta buscando e coloca 1 pra ambos

        # Se a gente quisesse tranformar esse gráfo num gráfo com peso, ou num grafo
        # unidirecional, você pode mudar o número ou comentar com um # em um dos dois self.graph... abaixo, respectivamente

        if vertice_source in list(self.vertices.keys()) and vertice_destination in list(self.vertices.keys()):

            vertice_source = self.vertices[vertice_source]
            vertice_destination = self.vertices[vertice_destination]

            if vertice_source == vertice_destination:
                print("You cannot connect a vertice to itself!")
                return

            self.graph[vertice_destination.position][vertice_source.position] = 1
            self.graph[vertice_source.position][vertice_destination.position] = 1
    
        else:
            print(f"Cannot connect vertices, since either vertice {vertice_source} or vertice {vertice_destination} do not exist")
            return

    def disconect_vertices(self, vertice_source, vertice_destination):

        # A operação inversa a conectar dados, colocando 0 no lugar de 1

        if vertice_source in list(self.vertices.keys()) and vertice_destination in list(self.vertices.keys()):

            vertice_source = self.vertices[vertice_source]
            vertice_destination = self.vertices[vertice_destination]

            if vertice_source == vertice_destination:
                print("You cannot disconect a vertice to itself!\n")
                return

            self.graph[vertice_destination.position][vertice_source.position] = 0
            self.graph[vertice_source.position][vertice_destination.position] = 0
        
        else:
            print(f"Cannot disconect vertices, since either vertice {vertice_source} or vertice {vertice_destination} do not exist\n")
            return

    def print_depth_search(self, vertex = None, visited = None):

        # Como dito antes, grafos tem as mesmas funções de busca de árvores, BFS e DFS, 
        # só que pra a gente não ficar preso num loop, a gente adiciona visited, uma 
        # lista, set ou dicionário em que a gente guarda os nodes que a gente já visitou

        if visited == None:
            visited = {}

        if not vertex:
            vertex = list(self.vertices.values())[0]
            visited[vertex] = True
            print(f"Performing Depth Search in node of data {vertex.data}:")
        
        elif not isinstance(vertex, Vertice):

            if vertex in self.vertices.keys():
                vertex = self.vertices[vertex]
                visited[vertex] = True
            else:
                print(f"The vertex {vertex} does not exist")
                return

        print(vertex.data)

        for id_connected_vertice, value in enumerate(self.graph[vertex.position]):
            
            if value == 1:
                connected_vertice = list(self.vertices.keys())[id_connected_vertice]

                if connected_vertice not in list(visited.keys()):
                    visited[connected_vertice] = True
                    self.print_depth_search(connected_vertice, visited)
                elif visited[connected_vertice] == False:
                    visited[connected_vertice] = True
                    self.print_depth_search(connected_vertice, visited)
    
    
    def print_breadth_search(self, vertex = None):

        queue = []
        visited = {}

        if not vertex:

            vertex = self.vertices[0]
            queue.append(vertex)

            print(f"Performing Breadth Search in node of data {vertex.data}:")

        elif not isinstance(vertex, Vertice):

            if vertex in self.vertices.keys():
                vertex = self.vertices[vertex]
                visited[vertex] = True
                queue.append(vertex)
            else:
                print(f"The vertex {vertex} does not exist")
                return

        while queue:
            vertex = queue.pop(0)

            if vertex not in list(visited.keys()) or visited[vertex] == False:

                print(vertex.data)
                visited[vertex] = True
                
                for vertex_position, value in enumerate(self.graph[vertex.position]):
                    
                    if value == 1:
                        queue.append(self.vertices[vertex_position])

    def print_graph(self):

        print("   " + "  ".join(map(str, [vertice + 1 for vertice in range(len(self.vertices))])))
        
        for vertice in self.vertices.values():
            print(f"{vertice.position + 1} [", end = "")
            print(", ".join(map(str, self.graph[vertice.position])), end=f"] ({vertice.position + 1}) {vertice.data}\n")

        print(end="\n")



if __name__ == "__main__":

    grafo = Graph()

    grafo.add_vertex(1)
    grafo.add_vertex(2)
    grafo.add_vertex(3)
    grafo.add_vertex(4)
    grafo.add_vertex(5)

    grafo.connect_vertices(1, 2)
    grafo.connect_vertices(2, 5)
    grafo.connect_vertices(4, 3)

    grafo.print_graph()

    #grafo.graph[0][1] = 5
    #print(grafo.graph[0][1])
    #grafo.print_graph()