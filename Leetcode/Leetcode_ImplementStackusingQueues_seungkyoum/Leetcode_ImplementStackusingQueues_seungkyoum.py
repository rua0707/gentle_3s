from typing import List
from collections import deque


# class MyStack:

#     def __init__(self):
#         self.q = deque()

#     def push(self, x: int) -> None:
#         self.q.append(x)
#         for _ in range(len(self.q) - 1):
#             self.q.append(self.q.popleft())

#     def pop(self) -> int:
#         return self.q.popleft()

#     def top(self) -> int:
#         return self.q[0]

#     def empty(self) -> bool:
#         return len(self.q) == 0

class MyStack:

    def __init__(self):
        self.stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> int:
        tmp = []
        while len(self.stk) > 1:
            tmp.append(self.stk.pop(0))
        ret = self.stk.pop(0)
        self.stk = tmp
        return ret

    def top(self) -> int:
        return self.stk[-1]

    def empty(self) -> bool:
        return len(self.stk) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.pop())
print(obj.pop())
