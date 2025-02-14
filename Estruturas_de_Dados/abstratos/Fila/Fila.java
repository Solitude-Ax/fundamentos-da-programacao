package Complexo.Fila;

public class Fila {
    
    public static void main(String[] args) {

        Queue fila = new Queue(4);

        fila.popQueue();

        fila.showQueue();

        fila.addQueue("Justin");
        fila.addQueue("Marcos");
        fila.addQueue("Narcisa");

        fila.showQueue();

        fila.popQueue();
        fila.popQueue();

        fila.addQueue("Roberto");
        fila.addQueue("Rodrigo");

        fila.showQueue();

        fila.popQueue();

        System.err.println(fila.popQueue());

        fila.showQueue();
}

}

class Queue {

    QueueNode head;
    QueueNode tail;
    int maximumSize;
    int numberElements = 0;

    Queue(int maximumSize, QueueNode head) {

        this.maximumSize = maximumSize;
        this.head = head;
        this.tail = head;

    };

    Queue(int maximumSize) {

        this(maximumSize, null);

    }

    Queue() {

        this(255, null);
    }

    void showQueue() {

        if (this.numberElements > 0) {
            System.out.print("[");

            QueueNode tempNode = this.head;

            while (tempNode != null) {

                System.err.print(tempNode.data + ", ");
                tempNode = tempNode.next;

            }

            System.out.println("\b\b]");

    } else {
        System.err.println("A fila está vazia");
        
    }

}

    void addQueue(String data) {

        if (this.maximumSize > this.numberElements) {

            QueueNode newNode = new QueueNode(data);

            if (this.tail != null) {
                this.tail.next = newNode;
                this.tail = newNode;
            } else {
                this.head = newNode;
                this.tail = newNode;
            }
            this.numberElements++;
        }
    }

    String popQueue() {
        if (this.numberElements > 0) {

            QueueNode removedNode = this.head;            

            this.head = this.head.next;
            this.numberElements--;
            
            return removedNode.data;
        } else {
            System.out.println("\nA fila está vazia");
            return null;
        }
    }
    
}

class QueueNode {

    String data;
    QueueNode next;

    public QueueNode(String data) {

        this.data = data;
        this.next = null;

    }

}