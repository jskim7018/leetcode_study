class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        # n의 factor 들의 모두 후보.
        # n으로 검증 가능 그러므로 n * sqrt(n) 가능
        n = len(nums)
        factors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
            if n % i == 0 and n//i != i:
                factors.append(n//i)

        sorted_nums = list(sorted(nums))

        ans = 0
        for k in factors:
            is_possible = True
            for i in range(0, n, k):
                curr = 0
                for j in range(1, k):
                    if nums[j-1+i] > nums[j+i]:
                        curr = j
                        break
                for j in range(k):
                    if sorted_nums[j+i] != nums[curr + i]:
                        is_possible = False
                        break
                    curr = (curr + 1) % k
                if not is_possible:
                    break
            if is_possible:
                ans += k

        return ans
