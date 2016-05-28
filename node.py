__author__ = 'lauramarshall'

import heapq


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.right = right
        self.left = left

    def display(self):
        print(self.data)

    def right(self, node):
        self.right = node

    def right(self):
        return self.right

    def left(self):
        return self.left

    def left(self, node):
        self.left = node

    def pre_order(self, node):
        if node is not None:
            node.display()
            self.pre_order(node.left)
            self.pre_order(node.right)
        else:
            return None

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            node.display()
        else:
            return None

    def level_order(self, node):
        q = []
        heapq.heappush(q, node)
        while 0 != len(q):
            node = heapq.heappop(q)
            node.display()
            if node.left:
                heapq.heappush(q, node.left)
            if node.right:
                heapq.heappush(q, node.right)


if __name__ == '__main__':
    non_node = Node(None, None, None)
    b = Node("b", None, None)
    c = Node("c", None, None)
    tree = Node("a", b, c)

    d = Node("d", None, None)
    e = Node("e", None, None)
    f = Node("f", None, None)
    g = Node("g", None, None)

    b.right = e
    b.left = d
    c.left = f
    c.right = g

    # test nil search in tree
    # print Node.in_order(non_node)

    print 'pre order traversal: entire tree'

    print tree.pre_order(tree)

    print 'pre order traversal: starts at b'

    print tree.pre_order(b)

    print 'post order traversal: entire tree'

    print tree.post_order(tree)

    print 'post order traversal: starts at b'

    print tree.post_order(b)

    print 'level order traversal'

    print tree.level_order(tree)