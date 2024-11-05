import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, val):
        self.val = val
        self.left: Node = None
        self.right: Node = None

    def IsBauble(self) -> bool:
        return (self.val % 2 == 1)

    def IsLight(self) -> bool:
        return (self.val % 2 == 0)

    def IsYellowLight(self) -> bool:
        return (self.val % 4 == 0)

    def IsRedLight(self) -> bool:
        return (self.val % 2 == 0) and (self.val % 4 != 0) 
    
    def IsLeaf(self) -> bool:
        return (self.left is None) and (self.right is None)
    
    def HaveLightChild(self):
        
        if self.left is not None:
            if self.left.IsLight(): 
                return True

        if self.right is not None:
            if self.right.IsLight(): 
                return True

        return False
            


class BST:
    def __init__(self):
        self.root : Node = None

    ###########################  member  ###########################
    
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
    
    ###########################  insert  ###########################
    
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


    ########################### display ###########################

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
    
    ###########################  delete  ###########################
    
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


        # Przypadek 4 - węzeł ma dwóch potomków
        elif (current.left is not None) and (current.right is not None):

            # znajdź następnika - maksymalny węzeł w lewym poddrzewie i jego rodzica
            successor_parent = current
            successor = current.left

            while True:
                if (successor.right is None): break
                successor_parent = successor
                successor = successor.right

            # Zastąp wartość węzła do usunięcia wartością następnika
            current.val = successor.val

            # Usuń następnika
            if (successor_parent.right == successor):
                successor_parent.right = successor.left

            elif (successor_parent.left == successor):
                successor_parent.left = successor.left

    ########################## Jest Oświetlona ##########################
    
    def JestOswietlona(self) -> bool:
        return self._jestOswietlona_recursive(self.root)
    

    def _jestOswietlona_recursive(self, node: Node) -> bool:

        if (node is None): 
            return True

        if (node.IsLeaf()): 
            return True

        if (not node.HaveLightChild()): 
            return False

        return (self._jestOswietlona_recursive(node.left)) and (self._jestOswietlona_recursive(node.right))
    
    ########################## Jest Równo oświetlona ##########################       

    def JestRownoOswietlona(self):
        return self._is_evenly_lit_helper(self.root) 
    
    
    def _count_lights(self, node):
        
        # Warunek stopu rekurencji
        if node is None:
            return (0, 0)
        
        # Liczymy swiatelka zolte i czerwone w prawym i lewym poddrzewie
        left_yellow, left_red = self._count_lights(node.left)
        right_yellow, right_red = self._count_lights(node.right)

        # Sumujemy liczbe swiatelek z prawego i lewego poddrzewa
        yellow_count = left_yellow + right_yellow
        red_count = left_red + right_red

        # Dodajemy jeszcze ewentualnie aktualny węzeł jeśli jest żółtym lub czerwonym światełkiem
        if node.IsYellowLight():
            yellow_count += 1
        elif node.IsRedLight():
            red_count += 1

        return (yellow_count, red_count)
    

    def _is_evenly_lit_helper(self, node):

        # Warunek stopu
        if node is None:
            return True

        # Zliczamy swiatelka czerwone i zolte
        yellow_count, red_count = self._count_lights(node)
       
        # Dalsza czesc rekurencji
        if abs(yellow_count - red_count) > 1:
            return False

        return self._is_evenly_lit_helper(node.left) and self._is_evenly_lit_helper(node.right)
    
    ################################### Jest Stylowa ###################################################
    
    def JestStylowa(self):
        return self._is_stylish(self.root)
    
    def _is_stylish(self, node):
        #Sprawdzamy, czy każda bombka ma żółtego liścia
        if node.IsBauble():
            return self._has_yellow_subtree(node)

        return self._is_stylish(node.left) or self._is_stylish(node.right)

    def _has_yellow_subtree(self, node):
        #Żeby miało żółte poddrzewo, wystarczy że ma żółtego liścia
        #War. stopu rekurencji
        if node is None:
            return False
        
        elif node.IsLeaf() and node.IsYellowLight():
            return True 
        
        elif node.IsLeaf() and (node.IsBauble or node.IsRedLight()):
            return False
        
        return self._has_yellow_subtree(node.left) or self._has_yellow_subtree(node.right)

    ################################# Jest Stabilna ##################################################
    
    def JestStabilna(self):
        return self._is_stable(self.root)
    
    def _is_stable(self, node):
        # war. stopu dla rekurencji
        if node is None:
            return True
        
        # Jest niestabilna jak różnica między poddrzewami: lewym i prawym jest większa niż 3
        if abs(sum(self._count_lights(node.left)) - sum(self._count_lights(node.right))) > 3:
            return False
        
        return self._is_stable(node.left) and self._is_stable(node.right)
    
    ################### Najdłuższy Łańcuch Kolorowy ###########################################
    def NajdluzszyLancuchKolorowy(self):
        return NotImplementedError
    
    def _is_colorful(self, chain):
        pass

    def _is_traditional(self, chain):
        yellow_lights = 0
        red_lights = 0

        # Zliczamy światełka czerwone i żółte
        for i in range (len(chain)):
            if chain[i] % 4 == 0:
                yellow_lights += 1
            else:
                red_lights += 1

        # Jest tradycyjna jeśli żółte = czerwone
        if yellow_lights == red_lights:
            return True
        return False

    def _all_chains(self):
        chains = []
        self._find_chains(self.root, [], chains)
        return chains

    def _find_chains(self, node, current_chain, chains):
        if node is None:
            return
        
        # Dodaj bieżący węzeł do ścieżki
        current_chain.append(node.val)

        # Jeśli to liść zapisz ścieżkę
        if node.left is None and node.right is None:
            chains.append(list(current_chain))

        # Przejdź w lewe poddrzewo i prawe poddrzewo
        if node.left:
            self._find_chains(node.left, current_chain, chains)
        if node.right:
            self._find_chains(node.right, current_chain, chains)

        # Usuń bieżący węzeł z ścieżki po powrocie z rekursji
        current_chain.pop()   
    
    ########################### Jest Elegancka ################################################
    def JestElegancka(self):
        return NotImplementedError
    
    def JestTradycyjna(self):
        return NotImplementedError
    ########################## Ile Łańcuchów Jednobarwnych ##################################

    def IleLancuchowJednobarwnych(self):
        chains = self._all_chains()
        count = 0
        for i in range (len(chains)):
            if self._is_monochromatic(chains[i]):
                count += 1
        return count

    def _is_monochromatic(self, chain):
        yellow_lights = 0
        red_lights = 0

        # Zliczamy światełka czerwone i żółte
        for i in range (len(chain)):
            if chain[i] % 4 == 0:
                yellow_lights += 1
            elif chain[i] % 2 == 0:
                red_lights += 1
                
        # Jest jednokolorowa jeśli wszystkie światełka są w jednym kolorze
        if (yellow_lights == 0 and red_lights != 0) or (yellow_lights != 0 and red_lights == 0):
            return True
        return False

    ################################ Jest Gotowa ##################################
    def JestGotowa(self):
        return NotImplementedError