import random


class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise ValueError
        data = random.randrange(len(self.items))
        temp = self.items[len(self.items) - 1]
        self.items[len(self.items) - 1] = self.items[data]
        self.items[data] = temp

        return self.items.pop(len(self.items) - 1)

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return not self.is_empty()

    def clear(self):
        for x in range(len(self.items)):
            self.items.pop()
