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


    def count_leaves(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return self.count_leaves(node.left) + self.count_leaves(node.right);

    def pre_order_clone(self, node):
        if node is None:
            return node

        temp = Node(None, None, None)
        temp.data = node.data
        temp.left = self.pre_order_clone(node.left)
        temp.right = self.pre_order_clone(node.right)

        return temp

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            node.display()
        else:
            return None

    def height(self, node):
        if node is None:
            return 0
        else:
            # find height of the left branch
            left_tree_height = self.height(node.left)
            # find the height of the right branch
            right_tree_height = self.height(node.right)

            # Use the larger one
            if left_tree_height > right_tree_height:
                return left_tree_height + 1
            else:
                return right_tree_height + 1

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

    print 'Height of tree'

    print tree.height(tree)

    print 'Count leaves'

    print tree.count_leaves(tree)

    tree_copy = tree.pre_order_clone(tree)

    print 'Copy of tree'

    print tree_copy.level_order(tree_copy)