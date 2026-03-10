from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 음수가 있기때문에 더 커져도 다시 작아질 수 있음.
        # freq_cnt로 해결 가능. 결국 현재 까지에서 뒤에 어디까지를, 끊어야지
        # k가되는지 봐야 하는데 끊을 수 있는 곳이 여러개. 여러개를 count로 저장하면 한번에 계산 가능.
        freq_cnt = defaultdict(int)
        freq_cnt[0] = 1

        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            need = prefix_sum - k
            ans += freq_cnt[need]
            freq_cnt[prefix_sum] += 1

        return ans
