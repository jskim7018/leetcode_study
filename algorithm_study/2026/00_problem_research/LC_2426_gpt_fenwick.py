class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res


class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)

        arr = [nums1[i] - nums2[i] for i in range(n)]

        # coordinate compression
        vals = set()
        for x in arr:
            vals.add(x)
            vals.add(x + diff)

        sorted_vals = sorted(vals)
        comp = {v: i + 1 for i, v in enumerate(sorted_vals)}  # 1-based index

        bit = Fenwick(len(sorted_vals))
        res = 0

        for x in arr:
            # query how many <= x + diff
            res += bit.query(comp[x + diff])

            # insert current value
            bit.update(comp[x], 1)

        return res
