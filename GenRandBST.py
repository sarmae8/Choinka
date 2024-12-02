from BST import *
import random

def GenRandBST(n : int) -> BST:
    tree = BST()

    if (n <= 0):
        raise Exception("n powinno być większe od 0.")

    elif (n < 1000):
        members = list(range(1,n+1,1))
        for i in range (n):
            member = random.choice(members)
            members.remove(member)
            tree.insert(member)
        return tree
    
    elif (n >= 1000):
        for i in range (n):
            tree.insert(random.randint(1,n))
        return tree