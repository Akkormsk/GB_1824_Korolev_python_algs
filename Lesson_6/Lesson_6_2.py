"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None or (root.left == None and root.right == None):
            return root
        q = deque()
        q.append(root)
        while q:
            next = None
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.right:
                    curr.right.next = next
                    q.append(curr.right)
                    next = curr.right
                if curr.left:
                    curr.left.next = next
                    q.append(curr.left)
                    next = curr.left
        return root

