import turtle

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root : Node = None

    ###########################  ----------  member  -----------  ##################################
    
    def member(self, val):
        return NotImplementedError
    
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


    def display(self, scale : int = 150):
        turtle.clear()
        turtle.speed(0)
        turtle.penup()
        if self.root:
            self._draw_tree(self.root, 0, 0, scale)
        turtle.hideturtle()
        turtle.done()

    def _draw_tree(self, node, x, y, offset):
        if node is not None:
            turtle.goto(x, y)
            turtle.write(node.val, align="center", font=("Arial", 10, "bold"))

            # Draw left child
            turtle.goto(x - offset, y - 65)
            turtle.pendown()
            turtle.goto(x, y - 15)
            turtle.penup()
            self._draw_tree(node.left, x - offset, y - 50, offset / 2)

            # Draw right child
            turtle.goto(x + offset, y - 65)
            turtle.pendown()
            turtle.goto(x, y - 15)
            turtle.penup()
            self._draw_tree(node.right, x + offset, y - 50, offset / 2)

        else:
            turtle.goto(x, y-35)
            turtle.write("null", align="center", font=("Arial", 10, "bold"))
    
    ###########################  ----------  delete  -----------  ##################################
    
    def delete(self, val):
        return NotImplementedError
    
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