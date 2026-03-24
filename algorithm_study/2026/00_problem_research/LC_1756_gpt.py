import math


# Square Root Decomposition
class MRUQueue:
    def __init__(self, n: int):
        self.B = int(math.sqrt(n)) + 1  # block size
        self.blocks = [list(range(i, min(i + self.B, n + 1))) for i in range(1, n + 1, self.B)]

    def fetch(self, k: int) -> int:
        val = None  # initialize
        for i, block in enumerate(self.blocks):
            if k <= len(block):
                val = block.pop(k - 1)
                break
            k -= len(block)

        if val is None:
            raise IndexError("k is out of bounds")

        # append val to the last block
        self.blocks[-1].append(val)

        # rebalance blocks
        for i in range(len(self.blocks) - 1):
            while len(self.blocks[i]) > self.B:
                self.blocks[i + 1].insert(0, self.blocks[i].pop())

        return val