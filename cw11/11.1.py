import random


def random_numbers(n):
    numbers = create_list(n)
    random.shuffle(numbers)
    return numbers


def almost_sorted_numbers(n):
    numbers = create_list(n)
    for i in range(1, n):
        x = random.randint(i - 1, i)
        numbers[i], numbers[x] = numbers[x], numbers[i]
    return numbers


def almost_sorted_reversed_numbers(n):
    numbers = almost_sorted_numbers(n)
    numbers.reverse()
    return numbers


def gaussian_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(random.gauss(0, 1))
    return numbers


def repeating_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(0, n // 2))
    random.shuffle(numbers)
    return numbers


def create_list(n):
    numbers = []
    for i in range(0, n):
        numbers.append(i)
    return numbers
