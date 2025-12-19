from typing import List
from collections import defaultdict


class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
           bench_to_students = defaultdict(set)

           ans = 0
           for student in students:
               bench_to_students[student[1]].add(student[0])
               ans = max(ans, len(bench_to_students[student[1]]))
           return ans
