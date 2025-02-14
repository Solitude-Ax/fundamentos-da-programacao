public class ListaEncadeada {

    public static void main(String[] args) {

        LinkedList<String> listaEncadeada = new LinkedList<>();
        listaEncadeada.addNode("Abc");
        listaEncadeada.addNode("Rock 'n Roll");
        listaEncadeada.addNode("Vinte cinco");

        listaEncadeada.removeNode("Rock 'n Roll");

        listaEncadeada.removeNode("Non Existent");

        listaEncadeada.removeNode("Abc");

        listaEncadeada.removeNode("Vinte cinco");

        LinkedList<String> emptyList = new LinkedList<>();
        emptyList.removeNode("");

        emptyList.addNode("First Node");
        emptyList.removeNode("First Node");
        emptyList.printList();



    }

}

class Node<Thing> {

    Thing data;
    Node<Thing> next;

    Node(Thing data) {
        this.data = data;
    }

}

class LinkedList<Thing> {

    Node<Thing> head;
    Node<Thing> tail;

    void addNode (Thing data) {

        Node<Thing> new_node = new Node<>(data);

        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
            this.printList();
        } else {
            this.tail.next = new_node;
            this.tail = this.tail.next;
            this.printList();
        }


    }

    void removeNode(Thing data) {

        if (this.head == null) {
            System.err.println("A lista ta vazia");
            return;
        }

        if (this.head.data.equals(data)) {
            this.head = this.head.next;
        } else {
            Node<Thing> current = this.head;
            
            while (current.next != null) {
                if (current.next.data == data) {
                    current.next = current.next.next;
                    this.printList();
                    return;
                }

                current = current.next;
            }

            System.err.println("O valor " + data + " não existe na lista");
            this.printList();
        }

    }

    void printList() {

        if (this.head != null) {
            Node<Thing> current = this.head;

            while (current != null) {

                System.out.print(current.data);
                
                if (current.next != null) {
                System.out.print(" -> ");
                } else {
                    System.out.print(" -> null\n");
                }

                current = current.next;

            }
        } else {
            System.err.println("A lista esta vazia");
        }
    }

}
