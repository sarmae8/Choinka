import os
from BST import BST
from GenRandBST import GenRandBST


def Continue(bst):
    os.system('cls')

    print("0) Wyświetl choinkę.")
    print()
    print("1) Czy jest oświetlona?")
    print("2) Czy jest równo oświetlona?")
    print("3) Czy jest stylowa?")
    print("4) Czy jest elegancka?")
    print("5) Czy jest tradycyjna?")
    print("6) Czy jest gotowa?")
    print("7) Ile ma łańcuchów jednobarwnych?")
    print("8) Jaka jest długość najdłuższego łańcucha kolorowego?")
    print()
    print("9) Powrót do menu głównego.")
    print("10) Zakończ program.")


def option1():
    n = int(input("Podaj liczbę n (liczba węzłów w drzewie): "))
    bst = GenRandBST(n)
    Continue(bst)


def option2():
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
        option1()

    elif opcja == "2":
        option2()

    elif opcja == "3":
        return
    
    else:
        os.system('cls')
        start(s=True)


def main():
    start()

if __name__ == "__main__":
    main()

