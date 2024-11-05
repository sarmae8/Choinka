from BST import *

def main():
    bst1  = BST() 
    m1 = [5,1,2,0.5,6,7,5.6]
    for i in range(len(m1)):
        bst1.insert(m1[i])
    
    print(f"Test 1: {bst1.JestStabilna() == True}")
    bst1.display()

    bst2 = BST()
    m2 = [1,2,3,4,5,6,7,8,9]
    for i in range (len(m2)):
        bst2.insert(m2[i])
    
    print(f"Test 2: {bst2.JestStabilna() == False}")
    bst2.display()

if __name__ == "__main__":
    main()