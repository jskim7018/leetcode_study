from typing import List

class KMP:
    def compute_lps(self, pattern):
        lps = [0] * len(pattern)
        j = 0

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j

        return lps

    def search(self, text, pattern):
        if not pattern:
            return []

        lps = self.compute_lps(pattern)
        result = []
        j = 0

        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]
            if text[i] == pattern[j]:
                j += 1
            if j == len(pattern):
                result.append(i - j + 1)
                j = lps[j - 1]

        return result


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # 그냥 kmp. kmp로 모든 a 위치 찾고, 모든 b 위치 찾은 다음 비교.
        # 사실상 그냥 string search 문제.

        kmp = KMP()
        a_indexes = set(kmp.search(s, a))
        b_indexes = set(kmp.search(s, b))

        indexes = list(a_indexes | b_indexes)
        left_closest_b_index = float('-inf')
        right_closest_b_index = float('inf')

        n = len(indexes)
        indexes.sort()
        ans_st = set()
        for i in range(n):
            l_idx = indexes[i]
            r_idx = indexes[n-i-1]
            if l_idx in b_indexes:
                left_closest_b_index = l_idx
            if r_idx in b_indexes:
                right_closest_b_index = r_idx
            if l_idx in a_indexes and abs(l_idx-left_closest_b_index) <= k:
                ans_st.add(l_idx)
            if r_idx in a_indexes and abs(r_idx-right_closest_b_index) <= k:
                ans_st.add(r_idx)

        return list(sorted(list(ans_st)))
