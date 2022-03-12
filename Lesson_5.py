from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def left_child(self, other):
        self.left = other

    def right_child(self, other):
        self.right = other

    def __repr__(self):
        return f'Node({repr(self.value)})'


class Tree:

    def __init__(self, root):
        self.root = root

    def dfs_preorder(self):
        start_node = self.root
        visited = []

        def helper(node):
            visited.append(node)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            return visited

        return helper(start_node)

    def dfs_postorder(self):
        start_node = self.root
        visited = []

        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                visited.append(node)
            return visited

        return helper(start_node)

    def dfs_inorder(self):
        start_node = self.root
        visited = []

        def helper(node):
            if node:
                helper(node.left)
                visited.append(node)
                helper(node.right)

            return visited

        return helper(start_node)

    def isSymmetric(self) -> bool:
        l_visited = []
        r_visited = []
        start = self.root

        def l_helper(node):
            if node:
                l_visited.append(node)
                l_helper(node.left)
                l_helper(node.right)
            return l_visited

        def r_helper(node):
            if node:
                r_visited.append(node)
                r_helper(node.left)
                r_helper(node.right)
            return r_visited

        return l_helper(start.left) == r_helper(start.right)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.left_child(b)
a.right_child(c)
b.left_child(d)
b.right_child(e)
g = Tree(a)
print(g.dfs_preorder())
print(g.dfs_postorder())
print(g.dfs_inorder())
print(g.isSymmetric())
