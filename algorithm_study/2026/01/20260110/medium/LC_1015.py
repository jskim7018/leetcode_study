class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        num = 1

        length = 1
        visited = set()
        while num % k != 0:
            if num % k in visited:
                return -1
            visited.add(num%k)
            num = num * 10 + 1
            num %= k
            length += 1

        return length
