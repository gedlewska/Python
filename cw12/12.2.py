def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    p = int((left + right) / 2)
    if left > right:
        return None
    if y == L[p]:
        return p
    elif y > L[p]:
        return binarne_rek(L, p + 1, right, y)
    else:
        return binarne_rek(L, left, p - 1, y)


arr = []
for x in range(100):
    arr.append(x)
print("Wyszukanie 36 wsrod elementow od 0 do 99")
print(binarne_rek(arr, 0, 99, 36))
print("wyszukanie 999 w wsrod elementow od 0 do 99")
print(binarne_rek(arr, 0, 99, 999))
