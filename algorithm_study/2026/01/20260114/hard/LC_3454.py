from typing import List


class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.length = [0] * (4 * self.n)

    def _push_up(self, node, l, r):
        if self.count[node] > 0:
            self.length[node] = self.xs[r] - self.xs[l]
        elif l + 1 == r:
            self.length[node] = 0
        else:
            self.length[node] = (
                self.length[node * 2] + self.length[node * 2 + 1]
            )

    def update(self, node, l, r, ql, qr, val):
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            self.count[node] += val
            self._push_up(node, l, r)
            return
        mid = (l + r) // 2
        self.update(node * 2, l, mid, ql, qr, val)
        self.update(node * 2 + 1, mid, r, ql, qr, val)
        self._push_up(node, l, r)

    def union_length(self):
        return self.length[1]


class Solution:
    def separateSquares(self, squares: List[List[int]]):
        events = []
        xs = set()

        for x, y, l in squares:
            xs.add(x)
            xs.add(x + l)
            events.append((y, 1, x, x + l))       # add
            events.append((y + l, -1, x, x + l))  # remove

        xs = sorted(xs)
        x_index = {v: i for i, v in enumerate(xs)}

        events.sort()
        st = SegmentTree(xs)

        prev_y = events[0][0]
        area = 0.0
        slabs = []  # (y_start, y_end, union_x_length)

        i = 0
        while i < len(events):
            y = events[i][0]
            dy = y - prev_y
            if dy > 0:
                ux = st.union_length()
                slabs.append((prev_y, y, ux))
                area += dy * ux
                prev_y = y

            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                st.update(1, 0, st.n, x_index[x1], x_index[x2], typ)
                i += 1

        half = area / 2
        cur = 0.0

        for y1, y2, ux in slabs:
            slab_area = (y2 - y1) * ux
            if cur + slab_area >= half:
                if ux == 0:
                    return y1
                return y1 + (half - cur) / ux
            cur += slab_area

        return slabs[-1][1]
