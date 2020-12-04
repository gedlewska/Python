import time

definition = {
    (0, 0): 0.5,
    (0, 1): 1,
    (1, 0): 0
}


def P(i, j):
    if (i, j) in definition.keys():
        return definition.get((i, j))
    if i == 0:
        return definition.get((0, 1))
    if j == 0:
        return definition.get((1, 0))
    else:
        definition[(i, j)] = 0.5 * (P(i - 1, j) + P(i, j - 1))
        return definition.get((i, j))


def P_recursion(i, j):
    if i == 0 and j == 0:
        return definition.get((0, 0))
    if i == 0:
        return definition.get((0, 1))
    if j == 0:
        return definition.get((1, 0))
    else:
        return 0.5 * (P_recursion(i - 1, j) + P_recursion(i, j - 1))


try:
    i = int(input("Write i: "))
    j = int(input("Write j: "))
except ValueError:
    print("Not a number")
else:
    start = time.time()
    answer = P(i, j)
    end = time.time()
    start_rec = time.time()
    answer_rec = P_recursion(i, j)
    end_rec = time.time()
    print("Dynamic programming result is:", answer, "and speed is:", end - start)
    print("Recursion result is:", answer_rec, "and speed is:", end_rec - start_rec)
