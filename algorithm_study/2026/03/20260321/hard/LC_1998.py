from typing import List


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
    def gcdSort(self, nums: List[int]) -> bool:
        # union find로 합할 수 있는 것들 모두 합하기.
        # 정렬시 있어야 할 위치 찾음.
        # 하나씩 가야할 자리를 확인 (만약 그래프 속하면, 즉 find의 root가 같으면 가능.).
        # 같은 그래프에 속하면 모두 서로의 위치를 자유롭게 오갈 수 있다는 것에 대한 증거/proof는?
        # union find를 어떻게 빠르게 만들지?

        n = len(nums)
        union_find = UnionFind(n)
        factor_root = dict()

        for idx, num in enumerate(nums):
            if num in factor_root:
                union_find.union(factor_root[num], idx)
            else:
                factor_root[num] = idx

            for factor1 in range(2, int(num**0.5) + 1):
                if num % factor1 == 0:
                    factor2 = num//factor1
                    if factor1 in factor_root:
                        union_find.union(factor_root[factor1], idx)
                    else:
                        factor_root[factor1] = idx
                    if factor2 in factor_root:
                        union_find.union(factor_root[factor2], idx)
                    else:
                        factor_root[factor2] = idx

        nums_w_idx = [(num,i) for i,num in enumerate(nums)]
        nums_w_idx.sort()

        for i, (num, prev_i) in enumerate(nums_w_idx):
            if union_find.find(prev_i) != union_find.find(i):
                return False

        return True
