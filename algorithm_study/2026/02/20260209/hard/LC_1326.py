from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # greedy?
        # 1.이전께 만약 더 멀거나 같은 곳을 커버하면 현재꺼는 뒤로도 앞으로도 아무런 기여가 없다.
        # 2.현재가 이전 것보다 더 멀다면? 이전꺼를 pop 해도 잘 되는지 확인.
        # 즉, 현재의 왼쪽이 이 이전의 오른쪽 보다 작거나 같으면.
        stck = []
        for i in range(len(ranges)):
            left = i - ranges[i]
            right = i + ranges[i]

            if stck and stck[-1][1] >= right:
                continue

            if left <= 0:
                stck = []
            else:
                while len(stck) >= 2 and left <= stck[-2][1]:
                    stck.pop()

            if stck and stck[-1][1] < n or not stck:
                stck.append([left, right])

        for i in range(1, len(stck)):
            if stck[i-1][1] < stck[i][0]:
                return -1

        return len(stck)
