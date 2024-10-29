from BST import *

def main():
    bst : BST = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(8)
    bst.insert(6)
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)

    bst.display(scale = 170)

if __name__ == "__main__":
    main()