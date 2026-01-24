from typing import List
from collections import defaultdict
import heapq


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)

        sums_by_id = defaultdict(int)
        versions_by_id = defaultdict(int)
        range_by_id = defaultdict(tuple)
        for i in range(n):
            sums_by_id[i] = nums[i]
            range_by_id[i] = (i, i)

        heap = []
        cnt_in_order = 0
        for i in range(1, n):
            if nums[i] >= nums[i-1]:
                cnt_in_order += 1
            heap.append((nums[i] + nums[i-1], (i-1, i), (0,0)))
        heapq.heapify(heap)
        union_find = UnionFind(n)

        op_cnt = 0
        curr_size = n
        while len(heap) > 0:
            if cnt_in_order+1 == curr_size:
                return op_cnt
            _sum, (left, right), (l_v, r_v) = heapq.heappop(heap)
            if versions_by_id[union_find.find(left)] != l_v or versions_by_id[union_find.find(right)] != r_v:
                continue
            if sums_by_id[union_find.find(left)] <= sums_by_id[union_find.find(right)]:
                cnt_in_order -= 1
            prev_left_sum = sums_by_id[union_find.find(left)]
            prev_right_sum = sums_by_id[union_find.find(right)]
            new_version = max(versions_by_id[union_find.find(left)], versions_by_id[union_find.find(right)]) + 1
            union_find.union(left, right)
            unioned_id = union_find.find(left)
            versions_by_id[unioned_id] = new_version
            sums_by_id[unioned_id] = _sum
            if left - 1 >= 0:
                left_id = union_find.find(left-1)
                if sums_by_id[left_id] <= prev_left_sum:
                    cnt_in_order -= 1
                if sums_by_id[left_id] <= _sum:
                    cnt_in_order += 1
                heapq.heappush(heap, (sums_by_id[left_id] + _sum,
                                      (range_by_id[left_id][0], right), (versions_by_id[left_id],
                                                                         versions_by_id[unioned_id])))
            if right + 1 < n:
                right_id = union_find.find(right+1)
                if prev_right_sum <= sums_by_id[right_id]:
                    cnt_in_order -= 1
                if _sum <= sums_by_id[right_id]:
                    cnt_in_order += 1
                heapq.heappush(heap, (sums_by_id[right_id] + _sum,
                                      (left, range_by_id[right_id][1]), (versions_by_id[unioned_id],
                                                                         versions_by_id[right_id])))
            range_by_id[unioned_id] = (left, right)
            curr_size -= 1
            op_cnt += 1
        return op_cnt
