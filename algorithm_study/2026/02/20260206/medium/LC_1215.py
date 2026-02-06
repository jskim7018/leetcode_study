from typing import List


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        # 결국 0에서 부터 시작해야함. 0에서 시작해서 low <= <= high range에 있으면 사용
        # high 이상 넘어가면 멈춤.
        ans = []

        # low 까지의 갯수 구하고, high 까지의 갯수 구한 다음. 빼는 것도 하나의 방법.
        def dfs(curr: int):
            if low <= curr <= high:
                ans.append(curr)
            elif curr > high:
                return

            last = curr % 10
            if last - 1 >= 0:
                dfs(curr * 10 + (last-1))
            if last + 1 <= 9:
                dfs(curr * 10 + (last+1))
        if low <= 0 <= high:
            ans.append(0) # zero is special case
        for i in range(1, 10):
            dfs(i)
        ans.sort()
        return ans
