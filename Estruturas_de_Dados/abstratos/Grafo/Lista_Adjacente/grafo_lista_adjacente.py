# A única coisa que tenho a falar aqui é que, ao invés de self.graph
# ser uma matriz de arrays, aqui ele é um dicionário que guarda referencias
# a os nodes que tem conexões aos seus vizinhos
#
# Exemplo:
#
# {1: [2], 2: [1, 3], 3: [2]}
# - 1 ta conectado a 2
# - 2 ta conectado a 1 e 3
# - 3 ta conectado a 2

class Vertice:

    def __init__(self, data):
        
        self.data = data
    
    def __repr__(self):
        return f"{self.data}"

class Graph:

    def __init__(self):
        
        self.vertice_data = {}
        self.graph = {}
    
    def add_vertex(self, data_vertex):

        if data_vertex not in self.vertice_data.keys():
            vertice = Vertice(data_vertex)

            self.vertice_data[data_vertex] = vertice
            self.graph[vertice] = []

            return vertice
    
    def connect_vertices(self, vertice_1, vertice_2):

        if vertice_1 in self.vertice_data and vertice_2 in self.vertice_data:

            vertice_1 = self.vertice_data[vertice_1]
            vertice_2 = self.vertice_data[vertice_2]

            if vertice_1 == vertice_2:
                print("You cannot connect a vertice to itself!")
                return

            if vertice_1 not in self.graph[vertice_2]:
                self.graph[vertice_2].append(vertice_1)

            if vertice_2 not in self.graph[vertice_1]:
                self.graph[vertice_1].append(vertice_2)
        
        else:
            print(f"Cannot connect vertices, since either vertice {vertice_1} or vertice {vertice_2} do not exist")
            return

    def disconect_vertices(self, vertice_1, vertice_2):

        if vertice_1 in self.vertice_data and vertice_2 in self.vertice_data:

            vertice_1 = self.vertice_data[vertice_1]
            vertice_2 = self.vertice_data[vertice_2]

            if vertice_1 == vertice_2:
                print("You cannot disconect a vertice to itself!\n")
                return

            if vertice_1 in self.graph[vertice_2]:
                self.graph[vertice_2].remove(vertice_1)

            if vertice_2 in self.graph[vertice_1]:
                self.graph[vertice_1].remove(vertice_2)
        
        else:
            print(f"Cannot disconect vertices, since either vertice {vertice_1} or vertice {vertice_2} do not exist\n")
            return

    def print_depth_search(self, vertex = None, visited = {}):

        graph = self.graph

        if not vertex:
            
            vertex = list(self.vertice_data.values())[0]

        elif vertex in self.vertice_data:

            vertex = self.vertice_data[vertex]

        if not visited:
            visited[vertex] = True
            print(f"Performing Depth Search in node of data {vertex.data}:")

        print(vertex.data)

        for connected_vertice in self.graph[vertex]:
            
            if connected_vertice not in visited:    
                visited[connected_vertice] = True
                self.print_depth_search(connected_vertice, visited)
            elif visited[connected_vertice] == False:
                visited[connected_vertice] = True
                self.print_depth_search(connected_vertice, visited)
            
        #print(end="\n")
    
    
    def print_breadth_search(self, vertex = None):

        graph = self.graph
        queue = []
        visited = {}

        if not vertex:

            vertex = list(self.vertice_data.values())[0]

            queue.append(vertex)

            print(f"Performing Breadth Search in node of data {vertex.data}:")

        elif vertex in self.vertice_data:

            vertex = self.vertice_data[vertex]

            queue.append(vertex)            

            print(f"Performing Breadth Search in node of data {vertex.data}:")

        while queue:
            vertex = queue.pop(0)

            if vertex not in visited or visited[vertex] == False:

                print(vertex.data)
                visited[vertex] = True
                
                for connected_vert in self.graph[vertex]:
                    queue.append(connected_vert)
        
        print(end="\n")

    def print_graph(self):

        for vertice in self.graph.keys():
            print(f"Vertice {vertice}:", end = " ")
            print(", ".join(map(str, self.graph[vertice])))

        print(end="\n")
    

if __name__ == "__main__":

    grafo = Graph()

    for x in range(5):
        grafo.add_vertex(x)

    grafo.connect_vertices(1, 3)
    grafo.connect_vertices(2, 3)
    grafo.connect_vertices(3, 1)

    grafo.connect_vertices(4, 0)

    grafo.print_depth_search()
    grafo.print_depth_search(3)

    grafo.print_breadth_search()
    grafo.print_breadth_search(3)

    grafo.print_graph()
    print(grafo.graph)