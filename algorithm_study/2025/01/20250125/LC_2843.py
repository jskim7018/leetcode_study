class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            if len(str(i)) % 2 == 0:
                i_str = str(i)
                if sum([int(x) for x in i_str[:len(i_str)//2]]) == \
                    sum([int(x) for x in i_str[len(i_str)//2:len(i_str)]]):
                    ans += 1
        return ans
