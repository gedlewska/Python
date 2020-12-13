class Node:
    """Klasa reprezentuje wezel drzewa binarnego"""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def bst_max(top):
    if top is None:
        raise ValueError("puste drzewo")

    while top.right is not None:
        top = top.right

    return top.data


def bst_min(top):
    if top is None:
        raise ValueError("puste drzewo")

    while top.left is not None:
        top = top.left

    return top.data
