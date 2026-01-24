class Solution:
    def minOperations(self, k: int) -> int:
        root = int(k ** 0.5)

        if root * root >= k:
            ans = root + root
        elif (root + 1) * root >= k:
            ans = root + root + 1
        else:
            ans = root + root + 2

        return ans - 2
