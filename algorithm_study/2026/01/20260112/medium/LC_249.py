from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        normalized_to_str = defaultdict(list)
        for s in strings:
            ops_cnt = ord('z') - ord(s[0])
            normalized_str = []
            for ch in s:
                normalized_str.append(chr((ord(ch)-ord('a') + ops_cnt) % 26 + ord('a')))
            normalized_to_str[''.join(normalized_str)].append(s)

        return list(normalized_to_str.values())
