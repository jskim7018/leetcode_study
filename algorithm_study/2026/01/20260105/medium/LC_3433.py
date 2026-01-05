from typing import List
from collections import defaultdict
import heapq


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        order = {
            "OFFLINE": 0,
            "MESSAGE": 1
        }

        events.sort(key=lambda x: (int(x[1]), order.get(x[0], 2)))

        user_mention_cnt = defaultdict(int)

        online_users = set(range(numberOfUsers))
        offline_users = []

        all_mention_cnt = 0
        for e in events:
            timestamp = int(e[1])
            while offline_users and offline_users[0][0] <= timestamp:
                online_users.add(heapq.heappop(offline_users)[1])

            if e[0] == "MESSAGE":
                users = e[2]
                if users == "ALL":
                    all_mention_cnt += 1
                elif users == "HERE":
                    for u in online_users:
                        user_mention_cnt[u] += 1
                else:
                    users_list = users.split(sep=" ")
                    users_list = [int(u[2:]) for u in users_list]
                    for u in users_list:
                        user_mention_cnt[u] += 1
            elif e[0] == "OFFLINE":
                user = int(e[2])
                online_users.remove(user)
                heapq.heappush(offline_users, (timestamp + 60, user))

        ans = []
        for i in range(numberOfUsers):
            ans.append(user_mention_cnt[i] + all_mention_cnt)

        return ans
