package Complexo.Arvore;

import java.util.ArrayList;

public class Arvore {
    
    public static void main(String[] args) {

        BinaryTree<Integer> tree = new BinaryTree<>();

        tree.addNode(1);
        tree.addNode(2);
        tree.addNode(3);

        tree.depthSearchPreOrder(tree.root);
        tree.depthSearchInOrder(tree.root);

        tree.depthSearchPostOrder(tree.root);

        tree.breadthSearch();

        tree.addNode(4);
        tree.addNode(5);

        tree.breadthSearch();
    }

}

class Node<Thing> {

    Thing data;
    Node<Thing> left;
    Node<Thing> right;

    Node(Thing data) {
        this.data = data;
    }

}

class BinaryTree<Thing> {

    Node<Thing> root;

    void printNodeTree(Node<Thing> node) {

        System.out.print("| Node Value: " + node.data);

        if (node.left == null) {
            System.out.print(" | Left: null");
        } else {
            System.out.print(" | Left: " + node.left.data);
        }

        if (node.right == null) {
            System.out.print(" | Right: null |");
        } else {
            System.out.print(" | Right: " + node.right.data);
        }

        System.out.println(" |");
    }

    void addNode(Thing data) {

        if (this.root == null) {
            this.root = new Node<>(data);
            return;
        }

        ArrayList<Node<Thing>> queue = new ArrayList<>();

        queue.add(this.root);
        
        while (!queue.isEmpty()) {

            Node<Thing> node = queue.getFirst();
            queue.removeFirst();

            if (node.left == null) {
                node.left = new Node<>(data);
                return;
            } else if (node.right == null) {
                node.right = new Node<>(data);
                return;
            } else {
                queue.add(node.left);
                queue.add(node.right);
            }

        }
        
    }

    void depthSearchPreOrder (Node<Thing> node) {

        if (this.root == null) {
            System.err.println("\nA arvore esta vazia");
        }

        if (node == null) {
            node = this.root;
        }

        System.out.println("\nDepth Search Pre Order");

        this.printNodeTree(node);

        if (node.left != null) {
            this.depthSearchPreOrder(node.left);
        }
        if (node.right != null) {
            this.depthSearchPreOrder(node.right);
        }
    }

    void depthSearchInOrder (Node<Thing> node) {

        if (this.root == null) {
            System.err.println("\nA arvore esta vazia");
        }

        if (node == null) {
            node = this.root;
        }

        System.out.println("\nDepth Search In Order");

        if (node.left != null) {
            this.depthSearchInOrder(node.left);
        }

        this.printNodeTree(node);

        if (node.right != null) {
            this.depthSearchInOrder(node.right);
        }
    }

    void depthSearchPostOrder (Node<Thing> node) {

        if (this.root == null) {
            System.err.println("\nA arvore esta vazia");
        }

        if (node == null) {
            node = this.root;
        }

        System.out.println("\nDepth Search Post Order");

        if (node.left != null) {
            this.depthSearchPostOrder(node.left);
        }
        if (node.right != null) {
            this.depthSearchPostOrder(node.right);
        }

        this.printNodeTree(node);

    }

    void breadthSearch() {

        if (this.root == null) {
            System.err.println("\nA arvore esta vazia");
            return;
        }

        
        ArrayList<Node<Thing>> queue = new ArrayList<>();
        
        queue.add(this.root);

        System.out.println("\nBreadth Search");

        while (!queue.isEmpty()) {

            Node<Thing> node = queue.getFirst();
            queue.removeFirst();

            if (node.left != null) {
                queue.add(node.left);
            } 
            if (node.right != null) {
                queue.add(node.right);
            }

            this.printNodeTree(node);
            
            
        }
    }
}