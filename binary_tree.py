# coding=utf-8


class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Binarytree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        """自上而下，从左往右添加"""
        node = Node(item)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if not cur_node.left:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breath_travel(self):
        """广度遍历"""
        if not self.root:
            return []

        result, queue = [], [self.root]
        while queue:
            cur_node = queue.pop(0)
            result.append(cur_node.item)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        print(result) 

    def preorder_travel(self, node):
        """前序遍历， 根-->左-->右"""
        if not node:
            return
        print(node.item, end=' ')
        self.preorder_travel(node.left)
        self.preorder_travel(node.right)

    def preorder_iter_travel(self):
        """前序遍历， 迭代版， 根-->左-->右"""
        if not self.root:
            return []
        result, stack = [], [self.root]

        while stack:
            # 使用栈维护节点访问顺序
            cur_node = stack.pop(0)
            if cur_node.right:
                stack.insert(0, cur_node.right)
            if cur_node.left:
                stack.insert(0, cur_node.left)
            result.append(cur_node.item)

        print(result)

    def inorder_travel(self, node):
        """中序遍历， 左-->根-->右"""
        if not node:
            return
        self.inorder_travel(node.left)
        print(node.item, end=' ')
        self.inorder_travel(node.right)

    def inorder_iter_travel(self):
        """中序遍历迭代版， 左-->根-->右"""
        if not self.root:
            return []
        result, stack = [], []
        p_node = self.root
        while stack or p_node:
            while p_node:
                stack.append(p_node)
                p_node = p_node.left
            cur_node = stack.pop()
            result.append(cur_node.item)
            if cur_node.right:
                p_node = cur_node.right
        print(result)

    def postorder_travel(self, node):
        """后序遍历， 左-->右-->根"""
        if not node:
            return
        self.postorder_travel(node.left)
        self.postorder_travel(node.right)
        print(node.item, end=' ')

    def postorder_iter_travel(self):
        """
           后序遍历：左-->右-->根
           """
        if not self.root:
            return []

        result, stack = [], [self.root]
        while stack:
            cur_node = stack.pop()
            result.append(cur_node.item)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)

        print(result[::-1])


if __name__ == '__main__':
    btree = Binarytree()
    btree.add(0)
    btree.add(1)
    btree.add(2)
    btree.add(3)
    btree.add(4)
    btree.add(5)
    btree.add(6)
    btree.add(7)
    btree.add(8)
    btree.add(9)

    print('=========breath_travel========')
    btree.breath_travel()

    print('=========preorder_travel========')
    btree.preorder_travel(btree.root)
    print('\n')
    btree.preorder_iter_travel()

    print('\n=========inorder_travel========')
    btree.inorder_travel(btree.root)
    print('\n')
    btree.inorder_iter_travel()

    print('\n=========postorder_travel========')
    btree.postorder_travel(btree.root)
    print('\n')
    btree.postorder_iter_travel()




