from collections import defaultdict


class Solution:
    def maxRequests(self, requests: list[list[int]], k: int, window: int) -> int:
        # sliding window.
        n = len(requests)

        user_counter = defaultdict(int)
        requests.sort(key=lambda x: x[1])
        ans = 0
        l = 0
        removed = [False] * n
        for r in range(n):
            user, time = requests[r]
            while removed[l]:
                l += 1
            while requests[l][1] < time - window:
                user_counter[requests[l][0]] -= 1
                l += 1

            if user_counter[user] < k:
                user_counter[user] += 1
                ans += 1
            else:
                removed[r] = True

        return ans
