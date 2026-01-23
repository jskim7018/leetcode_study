class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans = list(s)

        for i in range(len(ans)):
            left_dist_to_a = ord(s[i])-ord('a')
            right_dist_to_a = (ord('a') + 26) - ord(s[i])

            minim = min(left_dist_to_a, right_dist_to_a)
            if minim <= k:
                ans[i] = 'a'
                k -= minim
            else:
                ans[i] = chr(ord(ans[i]) - k)
                break

        return ''.join(ans)
