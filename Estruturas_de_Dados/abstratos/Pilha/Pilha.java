package Complexo.Pilha;

public class Pilha {
    
    public static void main(String[] args) {
        
        Stack pilha = new Stack();

        pilha.AddStack(1);
        pilha.AddStack(5);
        pilha.AddStack(327);

        pilha.ShowStack();

        pilha.PopStack();

        pilha.ShowStack();

        pilha.AddStack(27);

        pilha.ShowStack();

        pilha.PopStack();
        pilha.PopStack();

        pilha.ShowStack();

        pilha.AddStack(84);
        pilha.AddStack(55);
        pilha.AddStack(18);
        pilha.AddStack(97);

        pilha.ShowStack();

        pilha.PopStack();
        pilha.PopStack();

        pilha.ShowStack();


    }

}

class StackNode {

    int data;
    StackNode next;

    StackNode(int data, StackNode next) {

        this.data = data;
        this.next = next;

    }

    StackNode(int data) {
        this(data, null);
    }

}

class Stack {

    int maximumSize = 255;
    int numberElements = 0;
    StackNode topNode;

    Stack(int maximumSize, StackNode topNode) {
        this.maximumSize = maximumSize;
        this.topNode = topNode;
    }

    Stack(int maximumSize) {
        this(maximumSize, null);
    }

    Stack() {
        this(255, null);
    }

    void AddStack(int value) {
        if (this.maximumSize > this.numberElements) {
            StackNode newNode = new StackNode(value, this.topNode);
            this.topNode = newNode; 
            this.numberElements++; 

            System.out.println("O node " + topNode.data + " foi adicionado a pilha");

        } else {
            System.out.println("O stack ta cheio!");
        }
    }

    Integer PopStack() {

        if (this.numberElements > 0) {

            StackNode removedNode = this.topNode;
            this.topNode = this.topNode.next;

            System.out.println("O node " + removedNode.data + " foi removido da pilha");

            return removedNode.data;

        }

        else System.out.println("O stack esta vazio!");
        
        return null;

    }

    void ShowStack() {

        if (this.topNode != null) {
            
            StackNode temporary_node = this.topNode;
            System.out.print("[");

            while (temporary_node != null) { 

                System.out.print(temporary_node.data);

                if (temporary_node.next != null) {
                    System.out.print(", ");
                }

                temporary_node = temporary_node.next;
                
            }

            System.out.print("]");
            System.err.println("");

        } else {
            System.out.println("O stack esta vazio");
        }
    }
}