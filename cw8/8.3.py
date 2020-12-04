import random


def calc_pi(n):
    random.seed()
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            count += 1
    return 4 * count / n


try:
    n = int(input("Write n: "))
except ValueError:
    print("Not a number")
else:
    print("Result pi:", calc_pi(n))
