from typing import List


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)

        neg_pos = -1

        for i in range(len(balance)):
            if balance[i] < 0:
                neg_pos = i
                break

        if neg_pos == -1:
            return 0
        near_idx = 1

        ans = 0
        visited = set()
        while True:
            left = (neg_pos - near_idx + n) % n
            right = (neg_pos + near_idx) % n
            if left in visited and right in visited:
                break

            if left not in visited:
                if balance[left] <= -balance[neg_pos]:
                    ans += balance[left] * near_idx
                    balance[neg_pos] += balance[left]
                else:
                    ans += abs(balance[neg_pos]) * near_idx
                    return ans
                visited.add(left)
            if right not in visited:
                if balance[right] <= -balance[neg_pos]:
                    ans += balance[right] * near_idx
                    balance[neg_pos] += balance[right]
                else:
                    ans += abs(balance[neg_pos]) * near_idx
                    return ans
                visited.add(right)
            near_idx += 1

        if balance[neg_pos] >= 0:
            return ans
        else:
            return -1
