import heapq
from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # 모든 digit의 합이 3의 배수면 그 숫자는 3의 배수다 라는 사실을 이용.
        # 모두 더하면 셋 중하나가 됨. (나머지 -0, 1, 2)
        # 만약 0이면 그대로 사용하면됨. (1이면 홀수 하나 빼주면됨. 2면 짝수하나 빼주면됨(0보다 큰). 가장 작은 걸로)
        # 1인데 홀수가 없다면 짝수 2개를 빼고, 2인데 짝수가 없다면 홀수 2개를 뺀다.
        # TODO: <<<중요>>> 위에서 홀수가 아니라 3으로 나누었을때 나머지가 1인 것과 나머지가 2인 것이다.
        smallest_rem_one = []
        smallest_rem_two = []
        _sum = 0
        for digit in digits:
            _sum += digit
            if digit % 3 == 2 and (not smallest_rem_two or digit <= -smallest_rem_two[0]):
                heapq.heappush(smallest_rem_two, -digit)
                while len(smallest_rem_two) > 2:
                    heapq.heappop(smallest_rem_two)
            elif digit % 3 == 1 and (not smallest_rem_one or digit <= -smallest_rem_one[0]):
                heapq.heappush(smallest_rem_one, -digit)
                while len(smallest_rem_one) > 2:
                    heapq.heappop(smallest_rem_one)

        rem = _sum % 3

        to_delete = []
        if rem == 1:
            if len(smallest_rem_one) == 2:
                to_delete.append(-smallest_rem_one[1])
            elif len(smallest_rem_one) == 1:
                to_delete.append(-smallest_rem_one[0])
            else:
                if len(smallest_rem_two) == 2:
                    to_delete = [-e for e in smallest_rem_two]
                else:
                    return ""

        elif rem == 2:
            if len(smallest_rem_two) == 2:
                to_delete.append(-smallest_rem_two[1])
            elif len(smallest_rem_two) == 1:
                to_delete.append(-smallest_rem_two[0])
            else:
                if len(smallest_rem_one) == 2:
                    to_delete = [-e for e in smallest_rem_one]
                else:
                    return ""

        digits.sort(reverse=True)
        ans = []

        for digit in digits:
            if digit in to_delete:
                to_delete.remove(digit)
                continue
            ans.append(str(digit))
        if len(ans) and ans[0] == '0':
            return '0'
        else:
            return ''.join(ans)
