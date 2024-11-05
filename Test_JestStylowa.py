from BST import *

def main():
    bst0 = BST()
    bst0.insert(1)
    bst0.insert(4)
    bst0.insert(0)
    print(f"Test 1: {bst0.JestStylowa() == True}")

    bst1  = BST() 
    m1 = [5,1,2,0.5,6,7,5.6]
    for i in range(len(m1)):
        bst1.insert(m1[i])
    
    print(f"Test 2: {bst1.JestStylowa() == False}")

    bst2 = BST()
    m2 = [1,2,3,4,5,6,7,8]
    for i in range (len(m2)):
        bst2.insert(m2[i])
    
    print(f"Test 3: {bst2.JestStylowa() == True}")

if __name__ == "__main__":
    main()