from collections import defaultdict
import heapq


# Lazy deletion으로 쉽게 가능.
# version을 넣고, version이 아닌것은 버리고 version인 것만 사용.
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.max_pq = []
        self.id_to_version = defaultdict(int)

        for event_id, priority in events:
            self.id_to_version[event_id] += 1
            heapq.heappush(self.max_pq,
                           (-priority, event_id, self.id_to_version[event_id]))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.id_to_version[eventId] += 1
        heapq.heappush(self.max_pq,
                       (-newPriority, eventId, self.id_to_version[eventId]))

    def pollHighest(self) -> int:
        while self.max_pq and self.max_pq[0][2] != self.id_to_version[self.max_pq[0][1]]:
            heapq.heappop(self.max_pq)

        if self.max_pq:
            _, event_id, _ = heapq.heappop(self.max_pq)
            return event_id
        return -1

# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()