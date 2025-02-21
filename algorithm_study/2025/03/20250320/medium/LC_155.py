from collections import deque

class MinStack:

    def __init__(self):
        self.min_stack = deque()

    def push(self, val: int) -> None:
        if self.min_stack:
            self.min_stack.append((val, min(self.min_stack[-1][1],val)))
        else:
            self.min_stack.append((val, val))

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        return self.min_stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()