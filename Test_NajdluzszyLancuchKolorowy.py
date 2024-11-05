from BST import *

def main():
    bst = BST()
    bst.insert(10)
    bst.insert(12)
    bst.insert(14)
    bst.insert(16)
    print(f"Test 1: {bst.NajdluzszyLancuchKolorowy()==4}")

    bst1 = BST()
    bst1.insert(5)
    bst1.insert(4)
    bst1.insert(0)
    bst1.insert(2)
    bst1.insert(10)
    bst1.insert(12)
    print(f"Test 2: {bst1.NajdluzszyLancuchKolorowy() == 0}")
if __name__ == "__main__":
    main()