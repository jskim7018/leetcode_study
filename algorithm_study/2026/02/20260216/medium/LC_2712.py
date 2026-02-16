from typing import List


class Solution:
    def minimumCost(self, s: str) -> int:
        # dp로 구현하면 됨.
        # 반을 기준으로 앞 0과 1로 만들기 둘다 해보고 뒤도 마찬가지.
        # 앞 뒤의 결과들을 더한게 정답.
        half_len = len(s) // 2
        ans = [0, 0]

        def get_half_one_zero(is_from_left: bool, middle: int) -> List[int]:
            prev_one = 0
            prev_zero = 0
            for i in range(half_len + middle):
                curr_one = prev_one
                curr_zero = prev_zero
                if s[i if is_from_left else -1-i] == '0':
                    curr_one = (i+1) + prev_zero
                if s[i if is_from_left else -1-i] == '1':
                    curr_zero = (i + 1) + curr_one

                prev_one = curr_one
                prev_zero = curr_zero
            return [prev_zero, prev_one]

        for i, v in enumerate(get_half_one_zero(True, len(s) % 2)):
            ans[i] += v
        for i, v in enumerate(get_half_one_zero(False, 0)):
            ans[i] += v

        return min(ans)


# TODO: max min 사용해서 간단히 bit flip simulation 할 수 있었음
# class Solution:
#     def minimumCost(self, s: str) -> int:
#         n = len(s)
#         ans = 0
#
#         for i in range(1, n):
#             if s[i] != s[i - 1]:
#                 ans += min(i, n - i)  # TODO: 그냥 min, max로 어느것으로 할지 정하면 됨.
#
#         return ans
