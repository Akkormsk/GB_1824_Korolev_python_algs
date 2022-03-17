from collections import deque


# 1

class MinStack:

    def __init__(self):
        self.stack = []
        self._min = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self._min = val
        else:
            if val < self._min:
                self._min = val
        self.stack.append((val, self._min))

    def pop(self) -> None:
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# 2 не понял, в каком виде надо подавать вход на stepik, поэтому сделал тут

size, n = map(int, input().split(' '))
arr = [0] * n
dur = [0] * n
q = deque()
start = []
last_end = 0
for i in range(n):
    arr[i], dur[i] = map(int, input().split(' '))
    while q and q[0] < arr[i]:
        q.popleft()
    if len(q) >= size:
        start.append(-1)
        continue
    start.append(max(int(arr[i]), last_end))
    last_end = start[-1] + dur[i]
    q.append(last_end)

