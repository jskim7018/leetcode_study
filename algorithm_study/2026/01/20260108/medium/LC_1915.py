from collections import defaultdict


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mp = defaultdict(int)

        mp[0] = 1
        bitmask = 0

        ans = 0
        for ch in word:
            ch_int = ord(ch)-ord('a')
            bitmask = bitmask ^ (1 << ch_int)

            ans += mp[bitmask]

            for i in range(10):
                ans += mp[bitmask ^ (1 << i)]

            mp[bitmask] += 1

        return ans
