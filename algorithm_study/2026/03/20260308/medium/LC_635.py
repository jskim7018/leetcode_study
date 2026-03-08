from sortedcontainers import SortedList
from typing import List


# tuple로 저장. 정렬은 동적으로 sorted list로 한다.
class LogSystem:

    def __init__(self):
        self.sorted_list = SortedList()
        self.granularity_to_idx = {
            "Year": 0,
            "Month": 1,
            "Day": 2,
            "Hour": 3,
            "Minute": 4,
            "Second": 5
        }

    def put(self, id: int, timestamp: str) -> None:
        tuple_timestamp = tuple(int(t) for t in timestamp.split(':'))
        self.sorted_list.add((tuple_timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        granularity_idx = self.granularity_to_idx[granularity]

        start_tuple = [0] * 6
        end_tuple = [float('inf')] * 6
        for i, t in enumerate(start.split(':')):
            if i > granularity_idx:
                break
            start_tuple[i] = int(t)
        for i, t in enumerate(end.split(':')):
            end_tuple[i] = int(t)
            if i == granularity_idx:
                break
        start_tuple = tuple(start_tuple)
        end_tuple = tuple(end_tuple)

        left = self.sorted_list.bisect_left((start_tuple, float('-inf')))
        right = self.sorted_list.bisect_right((end_tuple, float('inf'))) - 1

        return [_id for t, _id in self.sorted_list[left:right+1]]

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)