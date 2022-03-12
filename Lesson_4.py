from collections import deque


# 1

class MinStack:

    def __init__(self):
        self.items = {}
        self._min = 0

    def push(self, val: int) -> None:
        if self.items == {}:
            self._min = val
        else:
            if val < self._min:
                self._min = val
        self.items[val] = self._min

    def pop(self) -> None:
        self.items.popitem()

    def top(self) -> int:
        return list(self.items.keys())[-1]

    def getMin(self) -> int:
        return self.items[self.top()]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 2 не понял, в каком виде надо подавать вход на stepik, поэтому сделал тут

size, n = map(int, input().split(' '))
arr = [0] * n
dur = [0] * n
q = deque()
start = []
last_end = 0
for i in range(n):
    arr[i], dur[i] = map(int, input().split(' '))
    if q:
        while q[0] < arr[i]:
            q.popleft()
        if len(q) >= size:
            start.append(-1)
            continue
    start.append(max(int(arr[i]), last_end))
    last_end = start[-1] + dur[i]
    q.append(last_end)

