import string
from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            digits = str(num)
            maxim = max(digits)
            enc_num = maxim*len(digits)
            ans += int(enc_num)
        return ans
