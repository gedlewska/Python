result = []


def flatten(sequence):
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flatten(item)
        else:
            result.append(item)
    return result


L = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(L))
