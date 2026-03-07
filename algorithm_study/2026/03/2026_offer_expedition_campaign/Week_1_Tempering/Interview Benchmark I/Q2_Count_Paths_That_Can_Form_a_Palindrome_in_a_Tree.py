from typing import List
from collections import defaultdict


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        # 길이가 even이면 모든 알파벳 갯수가 even이어야 함.
        # 길이가 odd이면 알파벳 하나만 odd이어야 함.
        # bit parity으로 만들기? (알파벳 26개) + frequency mapping
        n = len(parent)

        tree = defaultdict(list)
        for i in range(1,n):
            tree[parent[i]].append(i)

        parity_freq_cnt = defaultdict(int)
        parity_freq_cnt[0] += 1

        ans = 0

        def dfs(node: int, curr_parity_bitmask: int):
            nonlocal ans

            for u in tree[node]:
                bit_pos = ord(s[u]) - ord('a')
                new_parity_bitmask = curr_parity_bitmask ^ (1 << bit_pos)

                # For even
                ans += parity_freq_cnt[new_parity_bitmask]

                # For odd
                for i in range(26):
                    ans += parity_freq_cnt[new_parity_bitmask ^ (1 << i)]

                parity_freq_cnt[new_parity_bitmask] += 1
                dfs(u, new_parity_bitmask)

        dfs(0, 0)

        return ans
