def sum_seq(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        else:
            result += item
    return result


L = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("Sum:", sum_seq(L))
