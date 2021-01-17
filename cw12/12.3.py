def mediana_sort(L, left, right):
    Li = L[left:right]
    Li.sort()
    if len(Li) % 2 == 0:
        return Li[int((len(Li) / 2))]
    else:
        return Li[int((len(Li) + 1) / 2)]


arr = []
for x in range(100):
    arr.append(x)
print("Mediana 100 elementow")
print(mediana_sort(arr, 0, 99))
