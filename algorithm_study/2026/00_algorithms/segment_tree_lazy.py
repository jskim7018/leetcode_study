class LazySegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(nums, 1, 0, self.n - 1)

    def _build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
            return
        mid = (start + end) // 2
        self._build(nums, node * 2, start, mid)
        self._build(nums, node * 2 + 1, mid + 1, end)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _push(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:  # not a leaf
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update(self, left, right, value):
        self._update(1, 0, self.n - 1, left, right, value)

    def _update(self, node, start, end, left, right, value):
        self._push(node, start, end)

        if right < start or end < left:
            return

        if left <= start and end <= right:
            self.lazy[node] += value
            self._push(node, start, end)
            return

        mid = (start + end) // 2
        self._update(node * 2, start, mid, left, right, value)
        self._update(node * 2 + 1, mid + 1, end, left, right, value)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        self._push(node, start, end)

        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return (
            self._query(node * 2, start, mid, left, right)
            + self._query(node * 2 + 1, mid + 1, end, left, right)
        )
