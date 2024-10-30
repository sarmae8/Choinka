from BST import *
from random import randint

def GenRandBST(n : int) -> BST:
    tree = BST()
    for i in range (n):
        tree.insert(randint(1,100))
    return tree