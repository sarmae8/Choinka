import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, val):
        self.val: int = val
        self.left: Node = None
        self.right: Node = None

class BST:
    def __init__(self):
        self.root : Node = None

    ###########################  ----------  member  -----------  ##################################
    
    def member(self, val):                              # Funkcja odwołuje się do funkcji rekurencyjnej member_rec
        return self.member_rec(self.root, val)

    def member_rec(self, node, val):     
                       
        if node is None:                                # Jeżeli nie ma potomków to zwróć False
            return False
        
        elif node.val == val:                           # Jeżeli znaleźliśmy szukaną wartość to zwróć True
            return True     

        elif val < node.val:                            # Jeżeli "val" jest mniejsze niż "node.val" to szukamy w lewym potomku
            return self.member_rec(node.left, val)

        return self.member_rec(node.right, val)         # Jeżeli "val" jest większe niż "node.val" to szukamy w prawym potomku
    
    ###########################  ----------  insert  -----------  ##################################
    
    def insert(self, val):

        node : Node = self.root             # Zmienna `node` wskazuje na korzeń drzewa
        parentNode : Node = None            # `parentNode` to rodzic aktualnie przeglądanego węzła `node`.

        while node is not None:             # Przechodzimy przez drzewo

            if node.val == val:             # Jeśli wartość `val` już istnieje w drzewie, kończymy funkcję.
                return
            
            parentNode = node               # `parentNode` zapamiętuje rodzica `node`.

            if node.val < val:              # Jeśli `val` jest większe niż `node.val`, przechodzimy do prawego dziecka.
                node = node.right
            else:                           # W przeciwnym razie, przechodzimy do lewego dziecka.
                node = node.left

        newNode : Node = Node(val)          # Tworzymy nowy węzeł `newNode` dla wartości `val`.

        if parentNode is None:              # Jeśli `parentNode` jest `None`, drzewo jest puste, więc nowy węzeł staje się korzeniem.
            self.root = newNode

        elif parentNode.val < val:          # Jeśli `val` jest większe niż `parentNode.val`, wstawiamy `newNode` jako prawego potomka `parentNode`.
            parentNode.right = newNode

        else:                               # W przeciwnym razie, wstawiamy `newNode` jako lewego potomka `parentNode`.
            parentNode.left = newNode


    ########################### ------ display ------- ############################################

    def display(self):
        scale: int = 2
        
        # Create graph and layout
        G = nx.Graph()
        
        def add_edges(node, pos_x, pos_y, level=0):
            if node is None:
                return
            G.add_node(node.val, pos=(pos_x, pos_y))

            if node.left is not None:
                G.add_edge(node.val, node.left.val)
                add_edges(node.left, pos_x - scale / (2**level), pos_y - scale, level + 1)

            if node.right is not None:
                G.add_edge(node.val, node.right.val)
                add_edges(node.right, pos_x + scale / (2**level), pos_y - scale, level + 1)

        # Start the recursive edge adding from root
        add_edges(self.root, 0, 0)

        # Get node positions
        pos = nx.get_node_attributes(G, 'pos')
        
        # Draw the tree using matplotlib and networkx
        plt.figure(figsize=(10, 8))
        nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold")
        plt.title("Binary Search Tree")
        plt.show()
    
    ###########################  ----------  delete  -----------  ##################################
    
    def delete(self, val):
        # Korzeń drzewa
        current: Node = self.root
        parent: Node = None

        # Znajdź węzeł do usunięcia oraz jego rodzica
        while current is not None:
            if (current.val == val): break

            parent = current
            
            if val < current.val:
                current = current.left
            else:
                current = current.right


        # Jeśli węzeł nie został znaleziony
        if current is None:
            return  # Węzeł do usunięcia nie istnieje
        
        
        # Przypadek 1 - węzeł jest liściem
        elif (current.left is None) and (current.right is None):
            if (parent.left == current): parent.left = None
            if (parent.right == current): parent.right = None


        # Przypadek 2 - węzeł ma tylko lewego potomka
        elif (current.left is not None) and (current.right is None):
            if (parent.left == current): parent.left = current.left
            if (parent.right == current): parent.right = current.left


        # Przypadek 3 - węzeł ma tylko prawego potomka
        elif (current.right is not None) and (current.left is None):
            if (parent.left == current): parent.left = current.right
            if (parent.right == current): parent.right = current.right


        # Przypadek 4 - węzeł ma dwóch potomków TODO
        elif (current.left is not None) and (current.right is not None):
            left_node = current.left
            right_node = current.right


            
            # węzeł o maksymalnej wartości z lewego poddrzewa
            max_left_node: Node = current.left
            max_left_node_parent: Node
            while max_left_node.right is not None:
                max_left_node_parent = max_left_node
                max_left_node = max_left_node.right

            current.val = max_left_node.val
            max_left_node_parent.right = max_left_node.left

    ################################################################################################
    
    def JestOswietlona(self):
        return NotImplementedError
    
    def JestStylowa(self):
        return NotImplementedError
    
    def JestStabilna(self):
        return NotImplementedError
    
    def NajdluzszyLancuchKolorowy(self):
        return NotImplementedError
    
    def JestElegancka(self):
        return NotImplementedError
    
    def JestTradycyjna(self):
        return NotImplementedError
    
    def IleLancuchowJednobarwnych(self):
        return NotImplementedError

    def JestGotowa(self):
        return NotImplementedError