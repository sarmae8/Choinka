from BST import *

def main():

    bst  = BST()
    members = [17,11,13,15,16,18,28,23,21,19,5,1,8,6,7,24,25,20,4,14,22,12,29,30,2,3,26,27,9,10]
    for x in members:
        bst.insert(x)

    bst.display()

    bst.delete(23)
    bst.display()

if __name__ == "__main__":
    main()