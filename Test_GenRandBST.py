from BST import *
from GenRandBST import *


def main():
    bst = GenRandBST(30)
    bst.display()
    print(f"Ile łańcuchów jednobarwnych: {bst.IleLancuchowJednobarwnych()}")
    print(f"Jest elegancka: {bst.JestElegancka()}")
    print(f"Jest gotowa: {bst.JestGotowa()}")
    print(f"Jest oświetlona: {bst.JestOswietlona()}")
    print(f"Jest równo oświetlona: {bst.JestRownoOswietlona()}")
    print(f"Jest stablina {bst.JestStabilna()}")
    print(f"Jest stylowa: {bst.JestStylowa()}")
    print(f"Jest tradycyjna: {bst.JestTradycyjna()}")
    print(f"Najdłuższy łańcuch kolorowy: {bst.NajdluzszyLancuchKolorowy()}")

if __name__ == "__main__":
    main()