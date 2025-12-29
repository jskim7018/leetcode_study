import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        heap = []

        del_indexes = set()
        for i, ch in enumerate(s):
            if ch == '*' and heap:
                _, idx = heapq.heappop(heap)
                del_indexes.add(-idx)
            elif ch != '*':
                heapq.heappush(heap, (ch, -i))

        ans = []
        for i,ch in enumerate(s):
            if ch != '*' and i not in del_indexes:
                ans.append(ch)

        return ''.join(ans)
