# Projekt: Choinka w Drzewie BST

## Opis

Choinką jest drzewo `T` typu BST, którego węzły mają klucze będące liczbami naturalnymi.

- **Węzeł drzewa** jest bombką, jeśli jego klucz jest liczbą nieparzystą.
- **Węzeł drzewa** jest światełkiem, jeśli jego klucz jest liczbą parzystą:
  - Światełko jest **żółte**, jeśli klucz węzła jest liczbą podzielną przez 4.
  - Światełko jest **czerwone**, jeśli klucz węzła jest liczbą niepodzielną przez 4.

## Właściwości choinki
Choinka `T` jest:
- **oświetlona**, jeśli każdy węzeł wewnętrzny (tzn. nie będący liściem) ma potomka będącego światełkiem.
- **równo oświetlona**, jeśli dla każdego jej węzła `v`, różnica liczby świtełek żółtych i czerwonych co do modułu nie przekracza 1.
- **stylowa**, jeśli w przynajmniej jednym poddrzewie każdej bombki wszystkie światełka są żółte.
- **stabilna**, jeśli w każdym jej węźle `v` różnica liczby potomków w prawym i lewym poddrzewie jest co do modułu nie większa niż 3.

## Łańcuchy w drzewie
**Łańcuchem** w drzewie `T` nazywamy dowolną ścieżkę drzewa od korzenia do liścia. Łańcuch jest:
- **kolorowy**, jeśli wszystkie jego węzły (ewentualnie oprócz korzenia drzewa) są światełkami na przemian czerwonymi i żółtymi.
- **jednobarwny**, jeśli wszystkie jego światełka są tego samego koloru.
- **tradycyjny**, jeśli ma tyle samo światełek czerwonych co światełek żółtych.

## Wymagane metody BST

Należy zaimplementować drzewo BST ze standardowymi metodami wstawiania, usuwania i wyszukiwania klucza oraz następujące dodatkowe metody:

1. `JestOświetlona` - sprawdza, czy choinka `T` jest oświetlona lub równo oświetlona.
2. `JestStylowa` - sprawdza, czy choinka `T` jest stylowa.
3. `JestStabilna` - sprawdza, czy choinka `T` jest stabilna.
4. `NajdłuższyŁańcuchKolorowy` - zwraca długość najdłuższego łańcucha kolorowego na choince `T`.
5. `JestElegancka` - sprawdza, czy choinka `T` ma co najmniej tyle samo łańcuchów kolorowych co jednobarwnych.
6. `JestTradycyjna` - sprawdza, czy choinka `T` jest stabilna, równo oświetlona i ma przynajmniej jeden łańcuch tradycyjny.
7. `IleŁańcuchówJednobarwnych` - zwraca liczbę łańcuchów jednobarwnych na choince `T`.
8. `JestGotowa` - sprawdza, czy choinka `T` jest stabilna, oświetlona i ma przynajmniej jeden łańcuch kolorowy i jeden łańcuch jednobarwny.

## Wejście

Losowo (lub podane z klawiatury) zbudowane drzewo BST o minimum 30 węzłach.

## Wyjście

Program oferuje użytkownikowi opcje wyboru powyższych metod i udziela odpowiedzi na wybraną opcję. Dodatkowo dostępna jest możliwość wyświetlenia całego drzewa (z informacjami o każdym węźle: jego klucz oraz synowie).




