from typing import List
from collections import defaultdict


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        at_per_emp = defaultdict(list)
        for at in access_times:
            at_per_emp[at[0]].append((60*int(at[1][:2]) + int(at[1][2:])))

        ans = []
        for emp, ats in at_per_emp.items():
            ats.sort()
            for i in range(2, len(ats)):
                start = ats[i-2]
                end = ats[i]

                if end - start < 60:
                    ans.append(emp)
                    break

        return ans
