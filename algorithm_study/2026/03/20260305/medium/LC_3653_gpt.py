from collections import defaultdict
from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        # updates[k][rem] stores all updates where:
        # step size = k
        # index % k = rem
        updates = defaultdict(lambda: defaultdict(list))

        # --------------------------------------------------
        # STEP 1: Convert each query into a progression update
        # --------------------------------------------------
        for l, r, k, v in queries:

            # All affected indices satisfy:
            # i % k == l % k
            rem = l % k

            # Convert array index into progression index
            # Example: k=3, rem=1 → indices: 1,4,7,10...
            # progression index:
            # 1 -> 0
            # 4 -> 1
            # 7 -> 2
            start = (l - rem) // k
            end = (r - rem) // k

            # Store update for this progression
            updates[k][rem].append((start, end, v))

        # mult[i] will store total multiplier applied to nums[i]
        mult = [1] * n
        print(updates)
        # --------------------------------------------------
        # STEP 2: Process each (k, remainder) group
        # --------------------------------------------------
        for k in updates:
            for rem in updates[k]:

                # Number of elements in this progression
                # Example: rem=1, k=3, n=10 → [1,4,7]
                size = (n - rem + k - 1) // k

                # Difference array for multiplicative updates
                diff = [1] * (size + 1)

                # --------------------------------------------------
                # STEP 3: Apply range updates in difference array
                # --------------------------------------------------
                for s, e, v in updates[k][rem]:

                    # Multiply range start
                    diff[s] = diff[s] * v % MOD

                    # Cancel multiplication after range ends
                    if e + 1 < len(diff):
                        diff[e + 1] = diff[e + 1] * pow(v, MOD - 2, MOD) % MOD

                # --------------------------------------------------
                # STEP 4: Build prefix product and apply to array (sweep)
                # --------------------------------------------------
                cur = 1
                for i in range(size):

                    # accumulate multipliers
                    cur = cur * diff[i] % MOD

                    # convert progression index → real index
                    idx = rem + i * k

                    if idx < n:
                        mult[idx] = mult[idx] * cur % MOD

        # --------------------------------------------------
        # STEP 5: Apply multipliers to original array
        # --------------------------------------------------
        for i in range(n):
            nums[i] = nums[i] * mult[i] % MOD

        # --------------------------------------------------
        # STEP 6: Compute XOR of final array
        # --------------------------------------------------
        ans = 0
        for x in nums:
            ans ^= x

        return ans