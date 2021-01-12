import random


def bogo_sort(arr):
    n = len(arr)
    while not is_sorted(arr):
        shuffle(arr)


def is_sorted(arr):
    n = len(arr)
    for i in range(0, n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def shuffle(arr):
    n = len(arr)
    for i in range(0, n):
        x = random.randint(0, n - 1)
        arr[i], arr[x] = arr[x], arr[i]


tab = [6, 2, 9, 3, 1, 4, 8]
print("Array: ")
print(tab)
bogo_sort(tab)
print("Sorted array: ")
print(tab)
