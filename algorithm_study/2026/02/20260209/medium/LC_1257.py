from typing import List
from collections import defaultdict


class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # forms a tree, reverse edge.
        # It is same as finding LCA.
        # get ancestors of region1 and region2
        # check for the first common ancestor.

        tree = defaultdict(list)
        for region in regions:
            for r in region[1:]:
                tree[r].append(region[0])

        def get_ancestors(region: str, ancestors: List[str]):
            while region:
                ancestors.append(region)
                if tree[region]:
                    region = tree[region][0]
                else:
                    region = ""

        ancestors1 = []
        ancestors2 = []
        get_ancestors(region1, ancestors1)
        get_ancestors(region2, ancestors2)
        minim = min(len(ancestors1), len(ancestors2))
        # 뒤에서 부터 minim갯수 선택해서 사용.
        for a1, a2 in zip(ancestors1[-minim:], ancestors2[-minim:]):
            print(f'{a1}   {a2}')
            if a1 == a2:
                return a1

        return ""
