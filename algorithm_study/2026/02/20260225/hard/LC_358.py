from collections import Counter, deque
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s

        freq = Counter(s)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        cooldown = deque()  # (ready_index, -count, char)
        result = []
        index = 0

        while max_heap or cooldown:
            if max_heap:
                count, char = heapq.heappop(max_heap)
                result.append(char)
                count += 1  # decrease frequency (since negative)

                if count < 0:
                    cooldown.append((index + k, count, char))
            else:
                # No character available but still cooling → impossible
                return ""

            index += 1

            # If front of cooldown is ready, push back to heap
            if cooldown and cooldown[0][0] == index:
                _, ready_count, ready_char = cooldown.popleft()
                heapq.heappush(max_heap, (ready_count, ready_char))

        return "".join(result)
