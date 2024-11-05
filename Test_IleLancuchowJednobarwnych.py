from BST import *

def main():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(8)
    bst.insert(6)
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)
    print(f"Test 1: {bst.IleLancuchowJednobarwnych() == 4}")
          
    bst1 = BST()
    bst1.insert(5)
    bst1.insert(4)
    bst1.insert(0)
    bst1.insert(2)
    bst1.insert(10)
    bst1.insert(12)
    print(f"Test 2: {bst1.IleLancuchowJednobarwnych() == 0}")
if __name__ == "__main__":
    main()