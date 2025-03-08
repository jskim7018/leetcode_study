class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        currW = 0
        for i in range(k):
            if blocks[i] == 'W':
                currW += 1

        ans = currW

        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W':
                currW -= 1
            if blocks[i] == 'W':
                currW += 1
            ans = min(ans, currW)

        return ans
