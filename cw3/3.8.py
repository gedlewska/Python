import random

l1 = [random.randint(1, 50) for i in range(6)]
l2 = [random.randint(1, 50) for j in range(8)]
print("First list:", l1)
print("Second list:", l2)
common = set(l1)
intersection = common.intersection(l2)
print("Common part:", list(intersection))
total = set(l1).union(l2)
print("Sum:", list(total))
