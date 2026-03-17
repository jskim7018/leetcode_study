from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_groups = defaultdict(list)

        for str in strs:
            sorted_str = ''.join(list(sorted(str)))
            ana_groups[sorted_str].append(str)

        return list(ana_groups.values())
