from typing import List

def mod_pow(a: int, b: int, m: int) -> int:
    result = 1
    a %= m

    while b > 0:
        if b & 1:              # if b is odd
            result = (result * a) % m
        a = (a * a) % m        # square the base
        b >>= 1                # b = b // 2

    return result

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:

        ans = []
        for i,(a,b,c,m) in enumerate(variables):
            if mod_pow(mod_pow(a,b,10),c,m) == target:
                ans.append(i)

        return ans
