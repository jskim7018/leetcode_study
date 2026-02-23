import pytest


class Solution:
    def twoEggDrop(self, n: int) -> int:
        # 예: 14 면 14 부터 도전 -> 14에 1개 1~13 하나씩.
        # 그다음 13개만 가능 하다고 가정. 27에 도전.-> 그다음 12, 11,10,...
        # 즉, 목표 치가 a라고 하면 (a*(a+1))//2 >= n이면 가능.
        # 가장 작은 a를 찾을때 binary search로 효율화.
        # TODO: 수학적 방법 (O(1))도 이해하자. (근의 공식)

        l = 1
        r = n
        ans = n
        while l <= r:
            mid = (l+r)//2
            mid_seq_sum = (mid*(mid+1))//2
            if mid_seq_sum >= n:
                ans = mid
                r = mid-1
            else:
                l = mid + 1
        return ans


@pytest.mark.parametrize("n_input, expected", [
    (2, 2),
    (100, 14),
    (1, 1)
])
def test_twoEggDrop(n_input, expected):
    sol = Solution()
    assert sol.twoEggDrop(n_input) == expected
