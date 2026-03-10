class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stck = []

        for ch in s:
            if stck and stck[-1][0] == ch:
                stck[-1][1] += 1
            else:
                stck.append([ch, 1])

            if stck[-1][1] == k:
                stck.pop()

        return ''.join([ch*cnt for ch, cnt in stck])
