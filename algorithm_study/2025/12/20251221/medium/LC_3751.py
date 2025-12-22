class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        ans = 0
        for num in range(num1, num2+1):
            num_s = str(num)
            n = len(num_s)

            for i in range(1,n-1):
                if num_s[i-1] < num_s[i] > num_s[i+1]:
                    ans += 1
                elif num_s[i-1] > num_s[i] < num_s[i+1]:
                    ans += 1
        return ans
