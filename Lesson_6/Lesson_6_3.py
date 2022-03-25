in_array = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1


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
        return f'Node({repr(int(self.value))})'


class Tree:
    def __init__(self, arr):
        self.arr = arr[:]
        for i in range(len(arr)):
            self.arr[i] = Node(f'{arr[i]}') if arr[i] is not None else None
        self.root = self.arr[0]
        self.res = 0

    def make_tree(self):
        n = len(self.arr)
        for i in range(n):
            if 2 * i + 1 < n and self.arr[2 * i + 1]:
                self.arr[i].left_child(self.arr[2 * i + 1])
            if 2 * i + 2 < n and self.arr[2 * i + 2]:
                self.arr[i].right_child(self.arr[2 * i + 2])

    def dfs_pre_rec(self):
        start_node = self.root
        visited = []

        def helper(node):
            visited.append(node)
            helper(node.left)
            helper(node.right)
            return visited

        return helper(start_node)

    def dfs_pre_it(self):
        visited = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return visited

    def lca(self, q, p):

        def rec_tree(node):
            if not node:
                return False
            left = rec_tree(node.left)
            right = rec_tree(node.right)
            mid = node.value == str(p) or node.value == str(q)
            if mid + left + right >= 2:
                self.res = node
            return mid or left or right

        rec_tree(self.root)
        return self.res


def main():
    t = Tree(in_array)
    t.make_tree()
    print(t.lca(q, p))


if __name__ == '__main__':
    main()
