from typing import List
from collections import defaultdict
import heapq


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        # count에 대한 frequency max heap을 유지.
        # lazy하게 delete 함.
        n = len(nums)

        max_heap = []  # count

        ans = []
        id_to_count = defaultdict(int)
        cnt_frequency = defaultdict(int)
        # TODO: cnt_frequency 없이도 해보자.
        for i in range(n):
            _id = nums[i]
            _freq = freq[i]

            if _id in id_to_count:
                cnt_frequency[id_to_count[_id]] -= 1

            id_to_count[_id] += _freq

            cnt_frequency[id_to_count[_id]] += 1

            heapq.heappush(max_heap, -id_to_count[_id])

            while max_heap and cnt_frequency[-max_heap[0]] == 0:
                heapq.heappop(max_heap)

            if max_heap:
                ans.append(-max_heap[0])
            else:
                ans.append(0)

        return ans
