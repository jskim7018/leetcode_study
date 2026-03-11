from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # - 1을 더했다는 것은 무조건 bit에 1이 추가됨 그러므로. 1 총 비트 갯수 만큼 1을 더했다는 것.
        # - 2를 곱했다는 것은 모든 비트를 왼쪽으로 옮긴 것. 더해서 비트를 옮기는 것보다 무조건 곱해서 옮기는게 이득이기에 2를 곱한 갯수는 1이 가장 멀리 간곳을 기준으로 찾으면 됨.
        total_increments = 0
        max_bits = 0

        for num in nums:
            total_increments += num.bit_count()
            max_bits = max(max_bits, num.bit_length())

        # If max_bits is 0, return total_increments (which is also 0)
        return total_increments + max(max_bits - 1, 0)
