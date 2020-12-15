# coding=utf-8


class Stack(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self.size())

    def peek(self):
        return self._items[self.size()-1]

    def size(self):
        return len(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.size():
            return self._items.pop()
        else:
            return 0


def test():
    stack = Stack()
    print('stack is empty:', stack.is_empty())

    stack.push(100)
    stack.push(23)
    print('stack size:', stack.size())
    print('pop item:', stack.pop())

    stack.push(88)
    stack.push(99)

    print('stack peek item:', stack.peek())
    print('stack is empty:', stack.is_empty())


if __name__ == '__main__':
    test()
