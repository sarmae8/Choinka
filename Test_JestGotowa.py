from BST import *

def main():
    # Nie jest oświetlona
    bst = BST()
    print(f"Test 1: {bst.JestGotowa() == False}")
          
    # Nie ma łańcuchów      
    bst1 = BST()
    bst1.insert(5)
    bst1.insert(100)
    bst.insert(1)
    print(f"Test 2: {bst1.JestGotowa() == False}")

    # Ma wszystko
    bst2 = BST()
    bst2.insert(4)
    bst2.insert(2)
    bst2.insert(8)
    print(f"Test 3: {bst2.JestGotowa() == True}")

if __name__ == "__main__":
    main()