from typing import List
from collections import defaultdict


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        index_to_source = defaultdict(list)
        index_to_target = defaultdict(list)

        n = len(indices)
        for i in range(n):
            idx = indices[i]
            index_to_source[idx].append(sources[i])
            index_to_target[idx].append(targets[i])

        indices = list(set(indices))

        indices.sort()

        ans = []
        last_idx = -1
        for idx in indices:
            for source, target in zip(index_to_source[idx], index_to_target[idx]):
                if s[idx:idx+len(source)] == source:
                    ans.append(s[last_idx + 1: idx])
                    ans.append(target)
                    last_idx = idx + len(source) - 1
                    break
        ans.append(s[last_idx + 1: len(s)])

        return ''.join(ans)
