from collections import defaultdict
import heapq


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        # 총 갯수로 처리.
        # 미리 있는 애들 갯수 구함. 그 다음부터 작은 애들 순서로 하나씩 넣음.
        # 정렬 후 ?에 하나씩 넣어줌.
        # 총 갯수가 중요하기에 결국 총 갯수로 생각해서 푼다.

        min_heap = [[0, chr(ord('a')+i)] for i in range(26)]

        ans = [''] * len(s)
        q_indexes = []
        for i, ch in enumerate(s):
            if ch == '?':
                q_indexes.append(i)
            else:
                ans[i] = ch
                min_heap[ord(ch)-ord('a')][0] += 1

        heapq.heapify(min_heap)
        counter = defaultdict(int)

        for _ in range(len(q_indexes)):
            cnt, ch_to_add = heapq.heappop(min_heap)
            counter[ch_to_add] += 1
            heapq.heappush(min_heap, [cnt + 1, ch_to_add])

        sorted_chars = list(counter.items())
        sorted_chars.sort()
        q_curr_idx = 0
        for alph, cnt in sorted_chars:
            for _ in range(cnt):
                ans[q_indexes[q_curr_idx]] = alph
                q_curr_idx += 1

        return ''.join(ans)
