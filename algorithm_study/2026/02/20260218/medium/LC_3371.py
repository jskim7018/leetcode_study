from typing import List
from collections import defaultdict


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # TODO: 음수 고려 해야 하기 때문에 어려운 듯.
        # SUM 기준으로 돌아가면서 함. SUM과 나머지의 차를 구하고. 해당 차이를 만든 outlier가 있는지
        # hashmap으로 판정하면 끝.
        total_sum = 0
        counter = defaultdict(int)

        for num in nums:
            total_sum += num
            counter[num] += 1

        ans = float('-inf')
        for _sum in nums:
            rest = total_sum - _sum
            outlier_cand = rest - _sum
            if outlier_cand == _sum and counter[outlier_cand] >= 2:
                ans = max(ans, outlier_cand)
            elif outlier_cand != _sum and counter[outlier_cand] >= 1:
                ans = max(ans, outlier_cand)

        return ans
