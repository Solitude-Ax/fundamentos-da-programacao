import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;

public class GrafoListaAdjacente {

    public static void main(String[] args) {

        Graph<Integer> grafo = new Graph<>();

        for (Integer x = 0; x <= 5; x++) {
            grafo.addVertex(x);};

        grafo.connectVertices(1, 3);
        grafo.connectVertices(2, 3);
        grafo.connectVertices(3, 1);
        grafo.connectVertices(4, 0);

        grafo.printGraph();

        System.out.println("\nDepth Search:");
        grafo.printDepthSearch();

        System.out.println("\nBreadth Search");
        grafo.printBreadthSearch();

    }
    
}

class Vertice<Thing> {

    Thing data;

    Vertice(Thing data) {
        
        this.data = data;

    }
}

class Graph<Thing> {

    HashMap<Vertice<Thing>, ArrayList<Vertice<Thing>>> graph = new HashMap<>();
    HashMap<Thing, Vertice<Thing>> verticeData = new HashMap<>();

    void addVertex(Thing dataVertex) {

        if (!this.verticeData.containsKey(dataVertex)) {
            Vertice<Thing> vertice = new Vertice<>(dataVertex);
            ArrayList<Vertice<Thing>> list = new ArrayList<>();

            this.verticeData.put(dataVertex, vertice);
            this.graph.put(vertice, list);
        }
    }

    void connectVertices(Thing verticeSourceData, Thing verticeDestinationData) {

        if (this.verticeData.containsKey(verticeSourceData) && this.verticeData.containsKey(verticeDestinationData)) {

            Vertice<Thing> verticeSource = this.verticeData.get(verticeSourceData);
            Vertice<Thing> verticeDestination = this.verticeData.get(verticeDestinationData);

            if (verticeSource.equals(verticeDestination)) {
                System.err.println("You cannot connect a vertice to itself");
                return;
            }

            if (this.graph.containsKey(verticeSource) && this.graph.containsKey(verticeDestination)) {

                ArrayList<Vertice<Thing>> tempList = this.graph.get(verticeDestination);
                
                if (!tempList.contains(verticeSource)) {
                tempList.add(verticeSource);}

                tempList = this.graph.get(verticeSource);
                
                if (!tempList.contains(verticeSource)) {
                tempList.add(verticeDestination);}
            }
            else {

                ArrayList<Vertice<Thing>> tempList = new ArrayList<>();

                this.graph.put(verticeSource, tempList);
                this.graph.put(verticeDestination, tempList);

                tempList = this.graph.get(verticeSource);
                tempList.add(verticeDestination);

                tempList = this.graph.get(verticeDestination);
                tempList.add(verticeSource);
            }

        }
    }

    void disconnectVertices(Thing verticeSourceData, Thing verticeDestinationData) {

        if (this.verticeData.containsKey(verticeSourceData) && this.verticeData.containsKey(verticeDestinationData)) {

            Vertice<Thing> verticeSource = this.verticeData.get(verticeSourceData);
            Vertice<Thing> verticeDestination = this.verticeData.get(verticeDestinationData);

            if (verticeSource.equals(verticeDestination)) {
                System.err.println("You cannot disconnect a vertice to itself");
                return;
            }

            ArrayList<Vertice<Thing>> sourceArray = this.graph.get(verticeSource);
            ArrayList<Vertice<Thing>> destinationArray = this.graph.get(verticeDestination);

            if (sourceArray.contains(verticeDestination) && destinationArray.contains(verticeSource)) {
            sourceArray.remove(verticeDestination);
            destinationArray.remove(verticeSource);
            } else {
                System.err.println("Can't disconnect nodes " + verticeSource.data + " and " + verticeDestination.data + " because they aren't connected");
            }

        } else {
            System.err.println("Cannot disconect vertices, since either vertice " + verticeSourceData + " or vertice " + verticeDestinationData + "do not exist");
        }
    }

    void printDepthSearch(Vertice<Thing> vertex, HashMap<Vertice<Thing>, Boolean> visited) {

        if (vertex == null) {

            LinkedList<Vertice<Thing>> tempArray = new LinkedList<>(this.verticeData.values());
            vertex = tempArray.getFirst();
            
        } else if (this.verticeData.containsValue(vertex)) {

            vertex = this.verticeData.get(vertex.data);
            
        }

        if (visited == null) {

            visited = new HashMap<>();
            visited.put(vertex, true);
            System.out.println("Performing Depth Search in node of data " + vertex.data);

        }

        System.out.println(vertex.data);

        for (Vertice<Thing> connectedVertice : this.graph.get(vertex)) {

            if (!visited.containsKey(connectedVertice)) {
                visited.put(connectedVertice, true);
                this.printDepthSearch(connectedVertice, visited);
            } else if (visited.get(connectedVertice) == false) {
                visited.put(connectedVertice, true);
                this.printDepthSearch(connectedVertice, visited);
            }
        }
    }

    void printBreadthSearch(Vertice<Thing> vertice) {

        LinkedList<Vertice<Thing>> queue = new LinkedList<>();
        HashMap<Vertice<Thing>, Boolean> visited = new HashMap<>();

        if (vertice == null) {

            LinkedList<Vertice<Thing>> tempList = new LinkedList<>(this.verticeData.values());
            vertice = tempList.getFirst();
            queue.addLast(vertice);
            System.out.println("Performing Breadth Search in node of data " + vertice.data + ":");

        } else if (this.verticeData.containsValue(vertice)) {

            vertice = this.verticeData.get(vertice.data);
            queue.addLast(vertice);
            System.out.println("Performing Breadth Search in node of data " + vertice.data + ":");

        }

        while (!queue.isEmpty()) {

            vertice = queue.getFirst();
            queue.removeFirst();

            System.out.println(vertice.data);
            visited.put(vertice, true);

            for (Vertice<Thing> connectedVert : this.graph.get(vertice)) {
                if (!visited.containsKey(connectedVert) || visited.get(connectedVert) == false) {
                queue.addLast(connectedVert);
            }
            }
        }

    }

    void printDepthSearch() {
        this.printDepthSearch(null, null);
    }

    void printBreadthSearch() {
        this.printBreadthSearch(null);
    }

    void printGraph() {

        boolean firstPrinted = false;
        System.out.println("\nPrinting Vertices Conections in Graph:");

        for (Vertice<Thing> vertice : this.graph.keySet()) {
            System.out.print("Vertice " + vertice.data + ": ");

            for (Vertice<Thing> connectedVertice : this.graph.get(vertice)) {

                if (firstPrinted) {
                System.out.print(", " + connectedVertice.data);
                } else {
                    System.out.print(connectedVertice.data);
                    firstPrinted = !firstPrinted;
                }
            }
            firstPrinted = !firstPrinted;
            System.out.print("\n");
        }
        System.out.print("\n");
    }

}