from sortedcontainers import SortedList


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        sorted_list = SortedList()

        for i in range(1, n+1):
            sorted_list.add(i)

        curr = 0
        while len(sorted_list) > 1:
            curr = (curr + k - 1) % len(sorted_list)

            sorted_list.remove(sorted_list[curr])

        return sorted_list[0]
