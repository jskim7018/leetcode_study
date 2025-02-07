class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0

        for i in range(len(num1)):
            for j in range(len(num2)):
                n1 = int(num1[len(num1)-i-1])
                n2 = int(num2[len(num2)-j-1])
                n1 *= 10**i
                n2 *= 10**j

                ans += n1 * n2
        return str(ans)
