class Solution:
    def gcdSort(self, nums):
        n = len(nums)
        max_val = max(nums)

        # DSU
        parent = list(range(max_val + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Sieve to get smallest prime factor
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Factor + union
        for num in nums:
            x = num
            while x > 1:
                p = spf[x]
                union(num, p)
                while x % p == 0:
                    x //= p

        # Check if sortable
        sorted_nums = sorted(nums)
        for a, b in zip(nums, sorted_nums):
            if find(a) != find(b):
                return False

        return True