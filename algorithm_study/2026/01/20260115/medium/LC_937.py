from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort_func(log: str):
            sort_list = []
            log_split = log.split()
            log_id, first = log_split[0], log_split[1]
            is_letter = True
            if first.isdigit():
                is_letter = False

            if is_letter:
                sort_list.append(0)
            else:
                sort_list.append(1)
            if is_letter:
                sort_list.append(log[len(log_id):])
                sort_list.append(log_id)
            return tuple(sort_list)

        logs.sort(key=lambda log: sort_func(log))

        return logs
