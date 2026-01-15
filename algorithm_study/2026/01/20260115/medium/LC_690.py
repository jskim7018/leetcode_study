from typing import List



class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_to_employee = dict()

        for e in employees:
            id_to_employee[e.id] = e

        def dfs(id: int) -> int:
            e = id_to_employee[id]

            ret = e.importance

            for ne_id in e.subordinates:
                ret += dfs(ne_id)
            return ret

        return dfs(id)
