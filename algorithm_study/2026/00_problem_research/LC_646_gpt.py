class Solution:
    def findLongestChain(self, pairs):
        # we want to always get the one with smallest end each time greedily.
        # Because there is no benefit of replacing a bigger end with smaller end
        # when count is just going to be same since replacing wont increase count.
        pairs.sort(key=lambda x: x[1])

        curr_end = float('-inf')
        count = 0

        for a, b in pairs:
            if curr_end < a:
                count += 1
                curr_end = b

        return count