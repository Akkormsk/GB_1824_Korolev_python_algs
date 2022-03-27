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

    def lca(self, p, q):
        root = self.root

        def helper(node, p, q):
            if node.value == str(q) or node.value == str(p):
                return node
            if node.left:
                left = helper(node.left, p, q)
            if node.right:
                right = helper(node.right, p, q)
            if left and right:
                return node
            else:
                return left or right
        return helper(root, p, q)


def main():
    t = Tree(in_array)
    t.make_tree()
    print(t.lca(q, p))


if __name__ == '__main__':
    main()
