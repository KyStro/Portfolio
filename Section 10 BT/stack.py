# Implements a stack ADT
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return self._item == []

    def __str__(self):
        sval = "["
        for elem in self._items:
            sval += str(elem) + ", "
        sval += "]"
        return sval
