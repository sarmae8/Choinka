from BST import *

def main():
    bst = BST()
    bst.insert(33)
    bst.insert(13)
    bst.insert(47)
    print (f"Test 1: {bst.JestTradycyjna() == True}")

    bst1 = BST()
    bst1.insert(5)
    bst1.insert(4)
    bst1.insert(0)
    bst1.insert(2)
    bst1.insert(10)
    bst1.insert(12)
    bst1.insert(100)
    bst1.insert(101)
    bst1.insert(102)
    bst1.insert(103)
    bst1.insert(104)
    print (f"Test 2: {bst1.JestTradycyjna() == False}")
if __name__ == "__main__":
    main()