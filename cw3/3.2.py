L = [3, 5, 4] ; L = L.sort() #Sort() jest funkcją, a nie metodą, wiec nie może być wywołane na L.
x, y = 1, 2, 3 #Jest podane o jedną wartość za dużo.
X = 1, 2, 3 ; X[1] = 4 #Krotki są niemodyfikowalne, więc nie można przypisać wartości X[1].
X = [1, 2, 3] ; X[3] = 4 #Indeks 3 jest poza tablicą. Tablica ma rozmiar 3, więc ostatni indeks to 2.
X = "abc" ; X.append("d") #string nie ma metody append
L = list(map(pow, range(8))) #pow ma minimum 2 argumenty, na przykład pow(x, y) to x^y