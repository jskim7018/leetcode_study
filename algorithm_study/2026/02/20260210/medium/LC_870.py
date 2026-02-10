from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 양쪽 정렬해서 그리디로 가능한 방법이 있음. nums2 index 저장해두고 거기로 배치 해야함.
        # Tian Ji horse problem => Tian Ji (전기) is general of Qi dynasty in ancient China
        n = len(nums1)

        nums1.sort()
        nums2_with_index = [(num, i) for i, num in enumerate(nums2)]
        nums2_with_index.sort()

        ans = [-1] * n
        nums1_idx = 0
        other = []
        for i in range(n):
            while nums1_idx < n and nums1[nums1_idx] <= nums2_with_index[i][0]:
                other.append(nums1[nums1_idx])
                nums1_idx += 1

            if nums1_idx >= n:
                break

            ans[nums2_with_index[i][1]] = nums1[nums1_idx]
            nums1_idx += 1

        for i in range(n):
            if ans[i] == -1:
                ans[i] = other[-1]
                other.pop()

        return ans
