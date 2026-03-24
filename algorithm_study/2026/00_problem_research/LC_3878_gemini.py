from collections import defaultdict


class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        # last_pos[val] stores the most recent index where 'val' appeared
        last_pos = {}

        # curr_ors will store pairs of (value, leftmost_index)
        # that produce this OR result ending at the current element.
        curr_ors = []

        for r in range(n):
            val = nums[r]
            last_pos[val] = r

            # Update all existing OR segments with the new element
            next_ors = []
            # Start with the single element at index r
            temp_ors = curr_ors + [[val, r]]

            for i in range(len(temp_ors)):
                temp_ors[i][0] |= val
                # Merge segments with the same OR value to keep it O(log V)
                if not next_ors or next_ors[-1][0] != temp_ors[i][0]:
                    next_ors.append(temp_ors[i])

            curr_ors = next_ors

            # Now, for each distinct OR value segment starting at [start, end],
            # we check if that OR value 'v' exists in nums[l...r]
            # Since OR segments are (value, start_index), the segment covers
            # all left-starts from next_ors[i].start to next_ors[i+1].start - 1.
            for i in range(len(curr_ors)):
                v, start_idx = curr_ors[i]
                end_idx = curr_ors[i + 1][1] - 1 if i + 1 < len(curr_ors) else r

                # If the OR value 'v' appeared at index 'k',
                # then any subarray starting at l where l <= k is "good".
                if v in last_pos:
                    k = last_pos[v]
                    # The subarray starting at index 'l' is good if:
                    # 1. start_idx <= l <= end_idx
                    # 2. l <= k (the value v must be inside the subarray)

                    # Number of valid l's is max(0, min(end_idx, k) - start_idx + 1)
                    count = min(end_idx, k) - start_idx + 1
                    if count > 0:
                        ans += count


        return ans