class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)

        last_5_idx = -1
        last_0_idx = -1

        zero_cnt = 0
        for i in range(n-1, -1, -1):
            if num[i] == '5' and last_5_idx == -1:
                last_5_idx = i
            if num[i] == '0':
                zero_cnt += 1
                if last_0_idx == -1:
                    last_0_idx = i

        ans = n - zero_cnt
        for i in range(n-1):
            if num[i] == '2' or num[i] == '7':
                if i < last_5_idx:
                    ans = min(ans, n-i-2)
            elif num[i] == '5' or num[i] == '0':
                if i < last_0_idx:
                    ans = min(ans, n-i-2)

        return ans
