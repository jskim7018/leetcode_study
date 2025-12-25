class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        m = rows
        n = len(encodedText) // m

        ans = ''

        for j in range(n):
            curr_i = 0
            curr_j = j
            while curr_i < m and curr_j < n:
                ans += encodedText[curr_j+(curr_i*n)]
                curr_i += 1
                curr_j += 1

        return ans.rstrip(' ')
