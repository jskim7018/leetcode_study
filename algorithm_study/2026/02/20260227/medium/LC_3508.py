from typing import List
from collections import defaultdict, deque
import bisect
# timestamp 순서대로 들어와서 getCount 위해서 따로 정렬 불필요. (하지만 destination으로는 되어있어야 함.)
# 그냥 3가지 유지하면됨. 전체 packet queue, destination별 queue, packet set (duplicate detection 위해서)


class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packet_fifo = deque()
        self.destination_to_fifo = defaultdict(lambda: deque())
        self.curr_live_packet = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source,destination,timestamp)
        if packet in self.curr_live_packet:
            return False

        if len(self.packet_fifo) >= self.memoryLimit:
            rem_packet = self.packet_fifo.popleft()
            self.curr_live_packet.remove(rem_packet)
            self.destination_to_fifo[rem_packet[1]].popleft()

        if packet not in self.curr_live_packet:
            self.curr_live_packet.add(packet)
            self.destination_to_fifo[destination].append(timestamp)
            self.packet_fifo.append(packet)
            return True
        else:
            return False

    def forwardPacket(self) -> List[int]:
        if not self.packet_fifo:
            return []
        packet = self.packet_fifo.popleft()
        self.curr_live_packet.remove(packet)
        self.destination_to_fifo[packet[1]].popleft()

        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = bisect.bisect_right(self.destination_to_fifo[destination], startTime-1)
        right = bisect.bisect_right(self.destination_to_fifo[destination], endTime)-1
        return right-left + 1


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)