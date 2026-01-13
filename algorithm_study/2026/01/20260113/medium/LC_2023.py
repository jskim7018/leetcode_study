from typing import List
from collections import Counter, defaultdict


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        len_to_nums = defaultdict(Counter)

        t_len = len(target)

        st = set()
        for num in nums:
            len_to_nums[len(num)][num] += 1
            st.add(len(num))

        visited = set()

        ans = 0
        for length in st:
            if length in visited:
                continue
            visited.add(length)

            other_len = t_len - length
            for k, v in len_to_nums[length].items():
                if length == other_len:
                    len_to_nums[other_len][k] -= 1

                for k2, v2 in len_to_nums[other_len].items():
                    if k+k2 == target:
                        ans += v*v2

                if length == other_len:
                    len_to_nums[other_len][k] += 1

        return ans
