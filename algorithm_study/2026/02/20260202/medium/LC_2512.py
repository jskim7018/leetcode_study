from typing import List


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        p_feedback_st = set(positive_feedback)
        n_feedback_st = set(negative_feedback)

        n = len(student_id)
        score_list = []
        for i in range(n):
            report_words = report[i].split()
            score = 0
            for word in report_words:
                if word in p_feedback_st:
                    score += 3
                if word in n_feedback_st:
                    score -= 1
            score_list.append((score, student_id[i]))

        score_list.sort(key=lambda x: (-x[0], x[1]))

        ans = [s_id for _, s_id in score_list[:k]]

        return ans
