class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        last_pos = {}

        curr_ors = []

        for r in range(n):
            val = nums[r]
            last_pos[val] = r

            next_ors = []
            temp_ors = curr_ors + [[val, r]]

            for i in range(len(temp_ors)):
                temp_ors[i][0] |= val
                if not next_ors or next_ors[-1][0] != temp_ors[i][0]:
                    next_ors.append(temp_ors[i])

            curr_ors = next_ors

            for i in range(len(curr_ors)):
                v, start_idx = curr_ors[i]
                end_idx = curr_ors[i + 1][1] - 1 if i + 1 < len(curr_ors) else r

                if v in last_pos:
                    k = last_pos[v]

                    count = min(end_idx, k) - start_idx + 1
                    if count > 0:
                        ans += count

        return ans
