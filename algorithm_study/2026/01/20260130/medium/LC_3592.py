from typing import List


class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        curr_num_ways = [0] * (n+1)
        curr_num_ways[0] = 1

        coins = []
        for i in range(n):
            coin = i + 1
            if curr_num_ways[coin]+1 == numWays[i]:
                coins.append(coin)

                for j in range(coin, len(curr_num_ways)):
                    curr_num_ways[j] += curr_num_ways[j-coin]
            elif curr_num_ways[coin] != numWays[i]:
                return []

        return coins
