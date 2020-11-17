def odwracanie_iteracyjnie(L, left, right):
    mid = (right - left) // 2
    for item in range(mid):
        temp = L[right - item]
        L[right - item] = L[left + item]
        L[left + item] = temp
    return L


def odwracanie_rekurencyjnie(L, left, right):
    if left == right:
        return L
    temp = L[right]
    L[right] = L[left]
    L[left] = temp
    return odwracanie_rekurencyjnie(L, left + 1, right - 1)


L = list(range(1, 11))
print("List:", L)
print("Iterative:", odwracanie_iteracyjnie(L, 3, 7))
print("Recursive:", odwracanie_rekurencyjnie(L, 3, 7))
