# coding=utf-8

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return not bool(self._head)

    def length(self):
        if self.is_empty():
            return 0
        else:
            length = 1
            cur_node = self._head
            while cur_node.next:
                length += 1
                cur_node = cur_node.next
            return length

    def items(self):
        cur_node = self._head
        while cur_node:
            yield cur_node.item
            cur_node = cur_node.next

    def add(self, item):
        cur_node = Node(item)
        pre_head = self._head if self._head else None
        cur_node.next = pre_head
        self._head = cur_node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur_node = self._head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length()-1:
            self.append(item)
        else:
            node = Node(item)
            index = 0
            cur_node = self._head
            while cur_node.next:
                pre_node = cur_node
                cur_node = cur_node.next
                index += 1
                if pos == index:
                    node.next = cur_node
                    pre_node.next = node
                    break

    def remove(self, item):
        if self.is_empty():
            return None
        else:
            if item == self._head.item:
                self._head = self._head.next
            else:
                cur_node = self._head
                while cur_node:
                    pre_node = cur_node
                    cur_node = cur_node.next
                    if cur_node.item == item:
                        pre_node.next = cur_node.next
                        break

    def find(self, item):
        return item in self.items()


def print_single_list(single_list):
    tmp_list = []
    for item in single_list.items():
        tmp_list.append(item)
    print(tmp_list)


def test():
    single_list = SingleLinkList()
    print(single_list.is_empty())

    single_list.append(1)
    print(single_list.is_empty())

    single_list.append(3)
    single_list.append(100)
    print_single_list(single_list)

    single_list.add(200)
    print_single_list(single_list)

    print(single_list.length())

    single_list.insert(2, 88)
    print_single_list(single_list)

    single_list.remove(3)
    print_single_list(single_list)

    print(single_list.find(88))
    print(single_list.find(1000))


if __name__ == '__main__':
    test()



