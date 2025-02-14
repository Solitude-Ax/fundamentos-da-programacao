# É meio óbvio falar isso, mas na árvore,
# os nodes possuem 3 variavies: o dado, a esquerda e a direita.
# Essas duas últimas, são como a variavel próximo
# das estruturas anteriores. E apesar do nome diferente, age
# da mesma forma: armazenando qualquer node que você botar ali

class Node():
    def __init__(self, value):
        
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"{self.value}"

class Binary_Tree():
    def __init__(self, root:Node = None):
        
        self.root = root 
    
    def print_node_tree(self, node:Node):
        print(f"| Node Value: {node.value} | Left: {node.left} | Right: {node.right} |")

    def add_node(self, value):
        
        # Essa função básicamente usa uma função BFS (mais detalhes abaixo)
        # pra procurar um espaço vázio e colocar um node lá, priorizando 
        # sempre a esquerda

        # Eu esqueci de escreve essa função, mas um código para removes nodes
        # funcionária da mesma forma

        if not self.root:
            self.root = Node(value)
            print(f"Root of tree was created with value {self.root.value}")
            return
        
        queue = []
        queue.append(self.root)

        while queue:

            node = queue.pop(0)

            if not node.left:
                node.left = Node(value)
                return
            elif not node.right:
                node.right = Node(value)
                return
            else:
                queue.append(node.left)
                queue.append(node.right)

    def depth_search_preorder(self, node = None):

        if node is None:
            node = self.root
        
        if not node:
            print("A arvre ta vazia")
            return
    
        #print(node.value)
        self.print_node_tree(node)
                
        if node.left:
            self.depth_search_preorder(node.left)    
        if node.right:
            self.depth_search_preorder(node.right)
               
    def depth_search_inorder(self, node = None):
        
        if node is None:
            node = self.root
            
        if not node:
            print("A arvre ta vazia")
            return
        
        
        if node.left:
            self.depth_search_inorder(node.left)    
            
        #print(node.value)
        self.print_node_tree(node)
        
        if node.right:
            self.depth_search_inorder(node.right)

    def depth_search_postorder(self, node = None):
        
        if node is None:
            node = self.root
        if not node:
            print("A arvre ta vazia")
            return
        
        
        if node.left:
            self.depth_search_postorder(node.left)    
        if node.right:
            self.depth_search_postorder(node.right)
            
        #print(node.value)
        self.print_node_tree(node)

    def breadth_search(self):
        
        # Breadth Search é uma função de busca assim como DFS,
        # mas diferente das funções acima, aqui o código armazena
        # cada node num array (ou fila se preferir)

        # O código roda num While Loop, e continua nesse loop
        # até que essa fila esteja vazio.

        # Por conta dos primeiros visitados serem os mais próxmos
        # do node atual, isso faz com que o BFS faça 
        # uma varredura em níveis da árvore, ao invés de ir fundo
        # em cada galho, como no DFS

        queue = []

        if not self.root:
            return
        
        node = self.root
        queue.append(node)

        while queue:

            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            #print(node.value)
            self.print_node_tree(node)
        
        print(end="\n\n")

#        f
#       / \
#      b   g
#     / \    \
#   a   d    i
#       / \   /
#      c   e h

if __name__ == "__main__":

    bin_tree = Binary_Tree()

    bin_tree.add_node(1)
    bin_tree.add_node(3)

    print("Depth Pre Search:")
    bin_tree.depth_search_preorder()

    bin_tree.add_node(5)
    bin_tree.add_node(7)
    bin_tree.add_node(9)

    print("\nDepth In Search:")
    bin_tree.depth_search_inorder()

    bin_tree.add_node(11)
    bin_tree.add_node(13)
    bin_tree.add_node(15)

    print("\nDepth Post Search:")
    bin_tree.depth_search_postorder()

    bin_tree.add_node(17)
    bin_tree.add_node(19)
    bin_tree.add_node(21)

    print("\nBreadth Search:")
    bin_tree.breadth_search()