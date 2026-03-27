class Solution:

    # BFS. no need to explicitly get max depth
    def depthSumInverse(self, nestedList):
        queue = nestedList
        total_sum = 0
        level_sum = 0

        while queue:
            next_level = []

            for ni in queue:
                if ni.isInteger():
                    level_sum += ni.getInteger()
                else:
                    next_level.extend(ni.getList())

            total_sum += level_sum
            queue = next_level

        return total_sum