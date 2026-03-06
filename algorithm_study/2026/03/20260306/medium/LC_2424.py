# heap 사용시 가능 (lazy). => 메모리에 미리 넣어 두어야 하는 단점.
# 다른 방법은 없을까?
# Union find 가능? (union find w count), dict를 사용한 union find.
# TODO: heap도 아니고 그냥 pointer로도 가능.
# => 지금 없는 값을 가르키는 포인터를 사용하고. 업데이트 할때 있는 값까지 순회해서 가도록함.
# => 결국 모든 숫자는 총으로 봤을때 한번만 보기에 amortized complexity는 O(1)
# 전형적인 amortized/lazy 문제
from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.size = defaultdict(lambda: 1)

    def find(self, x: int) -> int:
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        size_rx, size_ry = self.size[rx], self.size[ry]
        if rx == ry:
            return False

        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

        self.size[self.find(x)] = size_rx + size_ry

        return True

    def get_size(self, x: int):
        return self.size[self.find(x)]


class LUPrefix:

    def __init__(self, n: int):
        self.curr_video_received = set()
        self.union_find = UnionFind()

    def upload(self, video: int) -> None:
        self.curr_video_received.add(video)
        if video - 1 in self.curr_video_received:
            self.union_find.union(video, video-1)
        if video + 1 in self.curr_video_received:
            self.union_find.union(video, video+1)

    def longest(self) -> int:
        if 1 in self.curr_video_received:
            return self.union_find.get_size(1)
        else:
            return 0

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()