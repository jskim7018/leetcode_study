from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = data.count(1)

        curr_zeros = data[0:window_size].count(0)
        ans = curr_zeros

        for i in range(window_size, len(data)):
            if data[i-window_size] == 0:
                curr_zeros-=1
            if data[i] == 0:
                curr_zeros+=1
            ans = min(ans,curr_zeros)

        return ans
