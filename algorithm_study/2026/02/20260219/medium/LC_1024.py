from typing import List
import heapq


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # max heap 사용. 가능한 것들 다 넣고 그중에서 오른쪽에 제일 긴애를 선택.
        # TODO: heap까지 사용할 필요 없이 그냥 바로 지금 가능 한 것중 farthest update.
        max_heap = []

        clips.sort()
        n = len(clips)

        curr_need = 0
        idx = 0
        ans = 0
        while curr_need < time:
            while idx < n:
                if clips[idx][0] <= curr_need:
                    heapq.heappush(max_heap, -clips[idx][1])
                else:
                    break
                idx += 1
            if not max_heap:
                return -1
            right = -heapq.heappop(max_heap)
            ans += 1
            if right > curr_need:
                curr_need = right

        return ans
