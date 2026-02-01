class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        curr = 0

        ans = 0
        for i in range(len(s)):
            if (curr*10 + int(s[i])) > k:
                ans += 1
                curr = 0
            curr = curr * 10 + int(s[i])
            if curr > k:
                return -1

        return ans + 1
