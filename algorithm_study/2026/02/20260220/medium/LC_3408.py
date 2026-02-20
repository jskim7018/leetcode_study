from typing import List
from collections import defaultdict
import heapq


class TaskManager:
    # taskid -> priority 배열 유지. lazy deletion. taskid task가 없으면 priority = -1.
    # 즉, remove시 task id -1으로.

    def __init__(self, tasks: List[List[int]]):
        self.task_id_to_p = defaultdict(lambda: -1)
        self.task_id_to_u = defaultdict(lambda: -1)
        self.tasks_by_p = []
        for u, t, p in tasks:
            self.task_id_to_p[t] = p
            self.tasks_by_p.append((-p, -t))
            self.task_id_to_u[t] = u
        heapq.heapify(self.tasks_by_p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.tasks_by_p, (-priority, -taskId))
        self.task_id_to_p[taskId] = priority
        self.task_id_to_u[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_id_to_p[taskId] = newPriority
        heapq.heappush(self.tasks_by_p, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        self.task_id_to_p[taskId] = -1
        self.task_id_to_u[taskId] = -1

    def execTop(self) -> int:
        # lazy deletion
        while (self.tasks_by_p and
               self.task_id_to_p[-self.tasks_by_p[0][1]] != -self.tasks_by_p[0][0]):
            heapq.heappop(self.tasks_by_p)

        if self.tasks_by_p:
            _, t_id = heapq.heappop(self.tasks_by_p)
            t_id = -t_id

            u_id = self.task_id_to_u[t_id]
            self.task_id_to_p[t_id] = -1
            self.task_id_to_u[t_id] = -1
            return u_id
        else:
            return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()