import random


class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            # 왼쪽에 있으면. (left)
            if k <= len(left):
                return quick_select(left, k)
            # 오른쪽에 있으면. (right)
            elif len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            else:
                # Pivot is in the pivot group (mid)
                # The pivot itself is the kth largest element.
                return pivot

        return quick_select(nums, k)
