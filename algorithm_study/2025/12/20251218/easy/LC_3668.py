from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_st = set(friends)

        ans = []
        for o in order:
            if o in friends_st:
                ans.append(o)

        return ans
