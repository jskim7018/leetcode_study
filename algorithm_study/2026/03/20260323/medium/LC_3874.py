class Solution:
    def validSubarrays(self, nums: list[int], k: int) -> int:
        # increase prefix, suffix 만들고 한다.
        peaks = [-1]

        n = len(nums)
        ans = 0
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                peaks.append(i)

                if len(peaks) >= 3:
                    l, m, r = peaks[-3], peaks[-2], peaks[-1]
                    ans += min(k+1, (m-l)) * min(k+1, (r-m))

        peaks.append(n)
        if len(peaks) >= 3:
            l, m, r = peaks[-3], peaks[-2], peaks[-1]
            ans += min(k+1, (m - l)) * min(k+1, (r - m))

        return ans
