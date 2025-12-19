from collections import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = Counter(s)

        if len(counter) <= k:
            return 0

        else:
            items = list(counter.items())
            items.sort(key=lambda x: x[1])

            ans = 0
            remove_cnt = len(counter) - k
            for i in range(remove_cnt):
                ans += items[i][1]

            return ans


# from collections import Counter
#
# class Solution:
#     def minDeletion(self, s: str, k: int) -> int:
#         counter = Counter(s)
#
#         if len(counter) <= k:
#             return 0
#
#         counts = sorted(counter.values())
#         remove_cnt = len(counter) - k
#         return sum(counts[:remove_cnt])
