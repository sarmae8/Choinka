from BST import *

def main():

    ### TEST 1

    bst  = BST()
    members = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    for x in members:
        bst.insert(x)

    print(f"Test 1: {bst.JestRownoOswietlona() == True}")


    ### TEST 2

    bst  = BST()
    members = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30]  
    for x in members:
        bst.insert(x)

    print(f"Test 2: {bst.JestRownoOswietlona() == True}")


    ### TEST 3

    bst  = BST()
    members = [16, 8, 24, 4, 12, 20, 28, 2, 6, 18, 26, 30, 1, 5]
    for x in members:
        bst.insert(x)

    print(f"Test 3: {bst.JestRownoOswietlona() == False}")


    ### TEST 4

    bst  = BST()
    members = [15, 10, 25, 5, 12, 20, 31, 3, 7, 9, 22, 28, 32]
    for x in members:
        bst.insert(x)

    print(f"Test 4: {bst.JestRownoOswietlona() == False}")
    

if __name__ == "__main__":
    main()