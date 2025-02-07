class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)

        s_i = 0

        arr = [[] for _ in range(numRows)]

        i = -1
        j = -1
        while s_i < n:
            i += 1
            j += 1
            for a in arr:
                a.append('')
            while i < len(arr):
                arr[i][j] = s[s_i]
                s_i += 1
                if s_i >= n:
                    break
                if i == len(arr)-1:
                    break
                i += 1

            while i >= 1 and s_i < n:
                i -= 1
                j += 1
                for a in arr:
                    a.append('')
                arr[i][j] = s[s_i]
                s_i += 1
                if s_i>=n:
                    break

        ans = ""
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] != '':
                    ans += arr[i][j]
        return ans