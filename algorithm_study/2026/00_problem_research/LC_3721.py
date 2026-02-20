from typing import List

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.min_val = [0] * (4 * n)
        self.max_val = [0] * (4 * n)

    def _push(self, v):
        if self.lazy[v] != 0:
            self.lazy[2*v] += self.lazy[v]
            self.min_val[2*v] += self.lazy[v]
            self.max_val[2*v] += self.lazy[v]
            self.lazy[2*v+1] += self.lazy[v]
            self.min_val[2*v+1] += self.lazy[v]
            self.max_val[2*v+1] += self.lazy[v]
            self.lazy[v] = 0

    def update(self, v, tl, tr, l, r, add):
        if l > r: return
        if l == tl and r == tr:
            self.lazy[v] += add
            self.min_val[v] += add
            self.max_val[v] += add
        else:
            self._push(v)
            tm = (tl + tr) // 2
            self.update(2*v, tl, tm, l, min(r, tm), add)
            self.update(2*v+1, tm+1, tr, max(l, tm+1), r, add)
            self.min_val[v] = min(self.min_val[2*v], self.min_val[2*v+1])
            self.max_val[v] = max(self.max_val[2*v], self.max_val[2*v+1])

    # TODO: why leftmost??
    def find_leftmost_zero(self, v, tl, tr, l, r):
        # We look for an index where the value is 0
        if l > r or self.min_val[v] > 0 or self.max_val[v] < 0:
            return -1
        if tl == tr:
            return tl
        self._push(v)
        tm = (tl + tr) // 2
        res = self.find_leftmost_zero(2*v, tl, tm, l, min(r, tm))
        if res == -1:
            res = self.find_leftmost_zero(2*v+1, tm+1, tr, max(l, tm+1), r)
        return res


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # TODO: 매우 자세하게 공부 필요. 일단 현재 코드 제대로 이해하자.
        # 왜 segment tree가 필요한지 정확하게 분석 필요.
        n = len(nums)
        st = SegmentTree(n)
        last_pos = {}
        max_len = 0

        for r in range(n):
            val = nums[r]
            prev = last_pos.get(val, -1)

            # Contribution: Even = +1, Odd = -1
            diff = 1 if val % 2 == 0 else -1

            # This distinct number started being "active" after its previous occurrence
            # So we update the balance for all start positions from (prev + 1) to r
            st.update(1, 0, n - 1, prev + 1, r, diff)

            # Find the earliest start position L in [0, r] where balance is 0
            l_idx = st.find_leftmost_zero(1, 0, n - 1, 0, r)

            if l_idx != -1:
                max_len = max(max_len, r - l_idx + 1)

            last_pos[val] = r

        return max_len
