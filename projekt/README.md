# Drzewo AVL

**Drzewo AVL** - jest to zrównoważone binarne drzewo poszukiwań (BST), w którym wysokość lewego i prawego poddrzewa
każdego węzła różni się co najwyżej o jeden.

## Operacje

Algorytmy podstawowych operacji na drzewie AVL przypominają te z binarnych drzew poszukiwań, ale są poprzedzane
lub następują po niech jedna lub wiecej rotacji. Koszt każdej operacji to O(log n)

### Wstawianie

Wstanianie do drzewa AVL wygląda tak samo jak w przypadku drzewa BST. Najpierw przeszukujemy drzewo w celu odszukania
miejsca wstawienia elementu, nastepnie wstawiamy ten element. Po wstawieniu elementu następuje sprawdzenie czy drzewo
jest zrównoważone tzn. czy wysokość pomiędzy prawym a lewym poddrzewem są równe: -1, 0, 1. Jeżeli mają wartości inne niż
podane powyżej następuję tak zwana rotacja drzewa. Mamy następujące rotacje:

**Rotacja RR** (ang. Right-Right)
W rotacji RR uczestniczą węzły A i B. Węzeł B zajmuje miejsce węzła A, węzeł A staje się lewym synem węzła B. Lewy syn
węzła B (BL) staje sie prawym synem węzla A.

**Rotacja LL** (ang. Left-Left)
Rotacja LL jest lustrzanym odbiciem rotacji RR. W rotacji uczestniczą dwa węzły A i B. Węzeł B zajmuje miejsce węzła A,
węzeł A staje się prawym synem węzła B.

**Rotacja RL** (ang. Right-Left)
Rotacja RL jest złożeniem rotacji LL i rotacji RR. Pierwza rotacja LL sprowadza gałąź drzewa do postaci dogodnej dla
następnej rotacji RR.

**Rotacja LR** (ang. Left-Right)
Rotacja LR jest złożeniem rotacji RR i LL. Jest lustrzanym odbiciem rotacji RL.

### Usuwanie

Usuwanie elementu z drzewa AVL odbywa się tak samo jak w przypadku drzewa BST (szukamy elementu do usuniecia a następnie
go usuwamy zachowując wszystkie własniści drzewa BST) po wykonanej operacji usuwania sprawdzamy czy drzewo jest
zrównoważone, jeśli nie wykonujemy rotacje jak w przypadku wstawiania.  

## Projekt

Moje drzewo AVL składa się z dwóch klas:

**Node**
Reprezentuje węzły drzewa.

**AVLTree**
Odpowiada za operacje na drzewie.

Klasa AVLTree zawiera podstawowe metody wstawienia elemntu do drzewa (insert) oraz usuwania elementu z drzewa (delete).

Dodatkowo klasa AVLTree zawiera dwie metody wypisujące drzewa:  
- print_tree - wypisuje drzewo w postaci drzewa (wizualizuje wygląd drzewa)    
- pre_order - wypisuje elementy drzewa w przejściu preOrder przez drzewo  

Metoda is_avl sprawdza czy drzewo jest postaci avl, sprawdzając różnicę wysokosci prawego i lewego poddrzewa.
Metoda is_balanced sprawdza czy drzewo jest postaci avl, sprawdzając całą jego strukturę.

Implementacja posiada również metodę get_size, która zwraca ilość elementów drzewa oraz get_height, która zwraca
wysokość drzewa.

Źródła:  
https://eduinf.waw.pl/inf/alg/001_search/0108.php
https://pl.wikipedia.org/wiki/Drzewo_AVL
https://www.tutorialspoint.com/data_structures_algorithms/avl_tree_algorithm.htm