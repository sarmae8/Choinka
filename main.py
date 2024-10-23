class Node:
    def __init__(self, val):
        self.v = val
        self.l = None
        self.r = None

class BST:
    def __init__(self):
        self.root = None
    
    def member(self, val):
        return NotImplementedError
    
    def insert(self, val):
        return NotImplementedError
    
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

def GenRandBST(n):
    return NotImplementedError