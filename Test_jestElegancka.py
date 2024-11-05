from BST import *

def main():
    bst = BST()
    print(f"Test 1: {bst.JestElegancka() == True}")
          
    bst1 = BST()
    bst1.insert(5)
    bst1.insert(100)
    bst.insert(1)
    print(f"Test 2: {bst1.JestElegancka() == False}")

    bst2 = BST()
    bst2.insert(4)
    bst2.insert(2)
    bst2.insert(8)
    print(f"Test 3: {bst2.JestElegancka() == True}")

if __name__ == "__main__":
    main()