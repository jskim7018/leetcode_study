from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        # TODO: bit 연산으로 나중에 다시 풀어보기. bit 연산을 잘 활용하면 loop 없이 최초의 0의 위치를 알 수 있음.
        for num in nums:
            final = -1

            bin_num = bin(num)[2:]

            curr_ans = ['0'] + list(bin_num)
            for j in range(len(curr_ans) - 1, -1, -1):
                if curr_ans[j] == '1':
                    continue
                else:
                    if j+1 < len(curr_ans):
                        curr_ans[j+1] = '0'
                        final = int(''.join(curr_ans), 2)
                    else:
                        final = -1
                    break

            ans.append(final)
        return ans
