class Tree:
    def __init__(self, n):
        self.parent = [0] * n
        self.rank = [0] * n
        for i in range(n):
            self.make_set(i)

    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return True
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[j_id] == self.rank[i_id]:
                self.rank[j_id] += 1


class Solution:
    def makeConnected(self, n, connections) -> int:
        m = 0
        t = Tree(n)
        for con in connections:
            if t.find(con[0]) == t.find(con[1]):
                m += 1
            else:
                t.union(con[0], con[1])
        l = len(connections)
        if l >= n - 1:
            return n - 1 - (l - m)
        else:
            return -1
