import os
import sys
from BST import BST
from GenRandBST import GenRandBST


def Continue(bst: BST):
    os.system('cls')

    text = """
0) Wyświetl choinkę. (jeśli drzewo jest bardzo duże to robisz to na własną odpowiedzialność :)

1) Czy jest oświetlona?
2) Czy jest równo oświetlona?
3) Czy jest stylowa?
4) Czy jest stabilna?
5) Czy jest elegancka?
6) Czy jest tradycyjna? 
7) Czy jest gotowa?
8) Ile ma łańcuchów jednobarwnych?
9) Jaka jest długość najdłuższego łańcucha kolorowego?

10) Powrót do menu głównego.
11) Zakończ program.

--------------------------------------------------------------------
"""

    print(text)

    while (True):
        opcja = input("Wybierz opcję: ")

        if opcja == "0":
            bst.display()
        elif opcja == "1":
            print(f"Jest oświetlona: {bst.JestOswietlona()}")
        elif opcja == "2":
            print(f"Jest równo oświetlona: {bst.JestRownoOswietlona()}")
        elif opcja == "3":
            print(f"Jest stylowa: {bst.JestStylowa()}")
        elif opcja == "4":
            print(f"Jest stablina {bst.JestStabilna()}")
        elif opcja == "5":
            print(f"Jest elegancka: {bst.JestElegancka()}")
        elif opcja == "6":
            print(f"Jest tradycyjna: {bst.JestTradycyjna()}")
        elif opcja == "7":
            print(f"Jest gotowa: {bst.JestGotowa()}")
        elif opcja == "8":
            print(f"Ile łańcuchów jednobarwnych: {bst.IleLancuchowJednobarwnych()}")
        elif opcja == "9":
            print(f"Najdłuższy łańcuch kolorowy: {bst.NajdluzszyLancuchKolorowy()}")
        elif opcja == "10":
            start()
        elif opcja == "11":
            sys.exit()
        else:
            print("Wybrano nieprawidłową opcję.")

        print()


##################################################################################################################################
##################################################################################################################################


def start(s = False):
    os.system('cls')

    text_powitalny = r"""
 _    _ _     _                                       _           _       _        
| |  | | |   (_)                                     | |         (_)     | |       
| |  | | |__  _  ___ _ __ __ _ _ __ ___  _   _    ___| |__   ___  _ _ __ | | _____ 
| |  | | '_ \| |/ _ \ '__/ _` | '_ ` _ \| | | |  / __| '_ \ / _ \| | '_ \| |/ / _ \
| |__| | |_) | |  __/ | | (_| | | | | | | |_| | | (__| | | | (_) | | | | |   <  __/
 \____/|_.__/|_|\___|_|  \__,_|_| |_| |_|\__, |  \___|_| |_|\___/|_|_| |_|_|\_\___|
                                         _ _/ |                                    
                                        |____/                                     """
    
    print(text_powitalny)
    print()

    if (s is True):
        print("Wybrano nieprawidłową opcję. Wybierz jeszcze raz.")
        print()

    print("1) Wygeneruj losowe drzewo BST.")
    print("2) Ręczne budowanie drzewa.")
    print("3) Zakończ program.")

    print()
    opcja = input("Wybierz opcję: ")
    
    if opcja == "1":
        start_option1()

    elif opcja == "2":
        start_option2()

    elif opcja == "3":
        sys.exit()
    
    else:
        os.system('cls')
        start(s=True)


def start_option1():
    n = int(input("Podaj liczbę n (liczba węzłów w drzewie): "))
    bst = GenRandBST(n)
    Continue(bst)


def start_option2():
    bst = BST()
    print("Wprowadź węzły jakie chcesz dodać. Aby zakończyć wstawianie wprowadź 'x'")
    while(True):
        x = input(": ")

        if (x.lower() in ["x", "'x'", "'x", "x'"]):
            break

        try:
            x = float(x)
            bst.insert(x)
        except:
            print("Podanej wartości nie można zrzutować na typ float.")

    Continue(bst)


def main():
    start()

if __name__ == "__main__":
    main()

