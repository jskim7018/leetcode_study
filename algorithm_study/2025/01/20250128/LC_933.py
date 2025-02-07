from collections import deque


class RecentCounter:

    def __init__(self):
        self.stack = deque()

    def ping(self, t: int) -> int:
        self.stack.append(t)
        while len(self.stack) != 0 and self.stack[0] < t-3000:
            self.stack.popleft()

        return len(self.stack)
