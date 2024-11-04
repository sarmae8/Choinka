from BST import *

def main():

    ### TEST 1

    bst  = BST()
    members = [100,50,20,110,150,220,270,130,134,60,24,14,8,34,134,158,162,224,38,124,104,102,108,154,4,2,6,16,12,22,30,32,28,54,52,68,66,70,64,120,128,106]
    for x in members:
        bst.insert(x)

    print(f"Test 1: {bst.JestOswietlona() == True}")



    ### TEST 2

    bst  = BST()
    members = [100,50,20,110,150,220,270,130,134,60,24,14,8,34,134,158,162,224,38,124,104,103,107,154,4,2,6,16,12,22,30,32,28,54,52,68,66,70,64,120,128,106]
    for x in members:
        bst.insert(x)

    print(f"Test 2: {bst.JestOswietlona() == False}")



    ### TEST 3

    bst  = BST()
    members = [101,50,20,110,150,220,270,130,134,63,24,14,8,34,134,158,162,224,38,124,104,103,108,154,4,2,6,16,12,22,30,32,28,54,52,68,66,73,64,120,128,106]
    for x in members:
        bst.insert(x)

    print(f"Test 3: {bst.JestOswietlona() == True}")



    ### TEST 4

    bst  = BST()
    members = [101,50,20,110,150,220,270,130,134,63,24,14,8,34,134,158,162,224,38,124,104,103,108,154,4,2,6,16,12,22,30,32,28,54,52,68,66,73,65,120,128,106]
    for x in members:
        bst.insert(x)

    print(f"Test 4: {bst.JestOswietlona() == False}")



    ### TEST 5

    bst  = BST()
    members = [1000,500,1500,259,300,350,200,1700,2000,1800,700,601,800,903,1251,1103,1350,1600]
    for x in members:
        bst.insert(x)

    print(f"Test 5: {bst.JestOswietlona() == False}")



    ### TEST 6

    bst  = BST()
    members = [1008,500,1500,259,300,356,200,1700,2008,1800,700,601,800,904,1251,1103,1352,1600]
    for x in members:
        bst.insert(x)

    print(f"Test 6: {bst.JestOswietlona() == True}")

    

if __name__ == "__main__":
    main()