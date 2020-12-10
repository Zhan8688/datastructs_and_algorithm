# coding=utf-8

class Node(object):
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next= None


class DLinkList(object):
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return not bool(self._head)

    def length(self):
        length = 0
        cur_node = self._head
        while cur_node:
            length += 1
            cur_node = cur_node.next
        return length

    def items(self):
        cur_node = self._head
        while cur_node:
            yield cur_node.item
            cur_node = cur_node.next

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            cur_head = self._head
            self._head = node
            node.next = cur_head
            cur_head.prev = self._head

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur_node = self._head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = node
            node.prev = cur_node
            self._tail = node

    def search(self, item):
        for i in self.items():
            if i == item:
                return True
        return False

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            index = -1
            cur_node = self._head
            while cur_node:
                index += 1
                if index == pos:
                    prev_node = cur_node.prev
                    node.next = cur_node
                    cur_node.prev = node
                    prev_node.next = node
                    node.prev = prev_node
                    break
                cur_node = cur_node.next

    def remove(self, item):
        if self.is_empty():
            return True
        else:
            cur_node = self._head
            if cur_node.item == item:
                self._head = None
                self._tail = None
                return
            while cur_node:
                if item == cur_node.item:
                    prev_node = cur_node.prev
                    next_node = cur_node.next
                    prev_node.next = next_node
                    if next_node:
                        next_node.prev = prev_node
                    else:
                        self._tail = prev_node
                    return

    def search(self, item):
        for i in self.items():
            if i == item:
                return True
        return False

    def reverse(self):
        cur_node = self._tail
        self._head = cur_node
        tail_node = None
        while cur_node:
            tail_node = cur_node
            prev_node = cur_node.prev
            cur_node.next = prev_node
            cur_node = prev_node
        self._tail = tail_node

    def init_list(self, item_list):
        for item in item_list:
            self.append(item)

    def print_list(self):
        item_list = []
        for item in self.items():
            item_list.append(item)
        print(item_list)


def print_dlink_list(dlink_list):
    tmp_list = []
    for i in dlink_list.items():
        tmp_list.append(i)
    print(tmp_list)


def test():
    dlink_list = DLinkList()
    print(dlink_list.is_empty())

    dlink_list.append(3)
    dlink_list.append(5)
    dlink_list.print_list()

    dlink_list.add(100)
    dlink_list.print_list()

    dlink_list.insert(2, 18)
    dlink_list.print_list()
    print(dlink_list.length())

    dlink_list.reverse()
    dlink_list.print_list()

    dlink_list2 = DLinkList()
    dlink_list2.init_list([10, 30, 50, 60])
    dlink_list2.print_list()

    print(dlink_list2.search(30))
    print(dlink_list2.search(233))


if __name__ == '__main__':
    test()
