package Complexo.Grafo.Matriz;

import java.util.ArrayList;
import java.util.HashMap;

public class GrafoMatriz {
    
    public static void main(String[] args) {
        
        Graph<Integer> grafo = new Graph<>();

        int[] abc = {1, 1, 1};

        grafo.addVertex(1);
        grafo.addVertex(2);
        grafo.addVertex(3);
        grafo.addVertex(4);
        grafo.addVertex(5);

        grafo.connectVertices(1, 2);
        grafo.connectVertices(2, 5);
        grafo.connectVertices(4, 3);

        grafo.printGraph();

    }

}

class Vertice<Thing> {

    Thing data;
    Integer position;

    Vertice(Thing data) {

        this.data = data;

    }
}

class Graph<Thing> {

    int positionCount = 0;

    HashMap<Thing, Vertice<Thing>> vertices = new HashMap<>();
    ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

    void addVertex(Thing dataVertex) {

        if (this.graph.isEmpty()) {

            Vertice<Thing> vertice = new Vertice<>(dataVertex);
            vertice.position = this.positionCount;
            this.vertices.put(dataVertex, vertice);

            ArrayList<Integer> vertexArray = new ArrayList<>(1);
            this.graph.addLast(vertexArray);
            this.positionCount += 1;


        } else if (!this.vertices.keySet().contains(dataVertex)) {

            Vertice<Thing> vertice = new Vertice<>(dataVertex);
            vertice.position = this.positionCount;
            this.vertices.put(dataVertex, vertice);

            ArrayList<Integer> vertexArray = new ArrayList<>();

            for (ArrayList<Integer> verticeList : this.graph) {

                vertexArray.addLast(0);

            }

            this.graph.add(vertexArray);
            this.positionCount += 1;
            
        } else {
            System.out.println("The Vertice " + dataVertex + " does not exist");
        }

    }

    void connectVertices(Thing verticeSourceData, Thing verticeDestinationData) {

        if (this.vertices.containsKey(verticeSourceData) && this.vertices.containsKey(verticeDestinationData)) {

            Vertice<Thing> verticeSource = this.vertices.get(verticeSourceData);
            Vertice<Thing> verticeDestination = this.vertices.get(verticeDestinationData);

            if (verticeSource.equals(verticeDestination)) {
                System.err.println("You cannot connect a vertice to itself!");
                return;
            }

            ArrayList<Integer> destinationArray = this.graph.get(verticeDestination.position);
            System.out.println("destinationArray: " + destinationArray + " this.graph: " + this.graph);

            //ArrayList<Integer> sourceArray = this.graph.get(verticeSource.position);
            //sourceArray.set(verticeDestination.position, 1);

            /*
            
            
            */
        } else {

            System.out.println("Cannot connect vertices, since either vertice " + verticeSourceData + " or vertice " + verticeDestinationData + " do not exist");
        }

    }

    void printGraph() {

      for (int x = 0; x < this.positionCount; x++) {

        System.err.print("   " + (x + 1) + "   ");

      }

      for (Vertice vertice : this.vertices) {

        System.out.print((vertice.position+1) + "[");
        
        for (Integer)

      }

    }
}