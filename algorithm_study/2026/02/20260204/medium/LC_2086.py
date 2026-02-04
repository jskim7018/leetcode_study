class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        i = 0
        ans = 0
        while i < n:
            if hamsters[i] == 'H':
                if i + 1 < n and hamsters[i+1] == '.':
                    i += 2
                    ans += 1
                else:
                    if i - 1 < 0 or hamsters[i-1] == 'H':
                        return -1
                    else:
                        ans += 1
            i += 1

        return ans
