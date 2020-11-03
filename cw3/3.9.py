sequenceList = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
result = []
for item in sequenceList:
    result.append(sum(item))
print("Sum:", result)
