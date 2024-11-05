from BST import *

def main():
    bst  = BST() 
    
    members = [15,7,3,2,5,4,6,11,13,14,12,9,8,10,30,20,50,17,25,40,110,35,45,70,220,31,37,42,47,150,250,46,27,1, 46.5, 45.5]
    for x in members:
        bst.insert(x)

    print(f"Test 1: {bst.member(7) == True}")

    print(f"Test 2: {bst.member(12) == True}")
    
    print(f"Test 3: {bst.member(350) == False}")
    
    print(f"Test 4: {bst.member(21) == False}")

if __name__ == "__main__":
    main()