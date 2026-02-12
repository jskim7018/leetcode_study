from collections import defaultdict


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # s2길이가 짧아서 완탐도 가능해보임. 하지만 더 나은 방법이 있을까? => (forward + backward contraction trick)
        # s2에 있는 character가 나오면 s2에서 해당하는 character를 모두 가장 짧은 걸로 업데이트 하기.
        n_s2 = len(s2)
        right_most_idx = [float('inf')] * n_s2
        minim = float('inf')
        minim_idx = (-1, -1)
        s2_ch_to_idx = defaultdict(list)

        for i in range(len(s2)-1, -1, -1):
            s2_ch_to_idx[s2[i]].append(i)

        for s1_i, ch in enumerate(s1):  # 10^4
            for i in s2_ch_to_idx[ch]:  # (최대가 100) 평균은 적음.
                if i - 1 >= 0:
                    right_most_idx[i] = right_most_idx[i-1]
                else:
                    right_most_idx[i] = s1_i
            if right_most_idx[n_s2-1] == float('inf'):
                continue
            if s1_i - right_most_idx[n_s2-1] + 1 < minim:
                minim = s1_i - right_most_idx[n_s2-1] + 1
                minim_idx = (right_most_idx[n_s2-1], s1_i)
        if minim == float('inf'):
            return ""
        else:
            return s1[minim_idx[0]:minim_idx[1]+1]

