class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # even - even => even
        # even - odd => odd
        # odd - odd => even
        # odd - even => odd

        # odd 하나라도 있으면 even 불가.
        min_odd = float('inf')
        is_all_even = True

        for num in nums1:
            if num % 2 == 1:
                is_all_even = False
                min_odd = min(min_odd, num)

        if is_all_even:
            return True

        for num in nums1:
            if num % 2 == 0:
                if num - min_odd < 1:
                    return False

        return True
