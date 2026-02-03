from typing import List
from collections import deque


class RideSharingSystem:

    def __init__(self):
        self.riders_queue = deque()
        self.drivers_queue = deque()
        # TODO: active riders 하나면 되는데 아래 처럼 2개 만들 필요 없었음.
        self.canceled_rider = set()
        self.rider_in_q = set()

    def addRider(self, riderId: int) -> None:
        self.riders_queue.append(riderId)
        self.rider_in_q.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers_queue.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders_queue and self.riders_queue[0] in self.canceled_rider:
            self.riders_queue.popleft()
        if self.riders_queue and self.drivers_queue:
            r = self.riders_queue.popleft()
            d = self.drivers_queue.popleft()
            self.rider_in_q.remove(r)
            return [d, r]
        else:
            return [-1,-1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.rider_in_q:
            self.canceled_rider.add(riderId)

# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)