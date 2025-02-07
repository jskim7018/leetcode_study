class Solution:
    def minimumSteps(self, s: str) -> int:
        black_idxs = []
        n = len(s)

        for i in range(n):
            if s[i] == '1':
                black_idxs.append(i)

        black_pos = n-1
        ans = 0
        for idx in black_idxs[::-1]:
            ans += black_pos-idx
            black_pos -=1
        return ans
