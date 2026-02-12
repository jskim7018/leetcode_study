class Solution:
    def numOfSubsequences(self, s: str) -> int:
        # 미리 LCT 갯수 계산
        # case 1: L을 넣으면 오른쪽에 CT 갯수 확인, L을 넣을 거면 가장 왼쪽에 넣는다.
        # case 2: C를 넣으면 왼쪽에 L의 갯수, 오른쪽에 T의 갯수 확인
        # case 3: T를 넣으면 왼쪽의 LC 갯수 확인. T를 넣을 거면 가장 오른쪽에 넣는다.

        # L -> L 갯수 LC -> C를 만났을때 이전의 L의 갯수, LCT -> T를 만났을때 이전의 LC 갯수.

        # 혹은 c를 만날때 마다 왼쪽의 l의 갯수, 오른쪽의 t의 갯수를 곱해준 것을 더하면 됨.
        # 즉 l, t의 prefix sum을 구함. case1을 왼쪽에 항상 l이 하나 있는 것으로 하고 case3는 항상 r이 오른쪽에 더 있는것으로 함.
        # case2의 경우 각 위치에 c를 넣어보면서 기존 lct 갯수 + 새로 찾은 lct 갯수의 max를 사용.
        # TODO: LCT dp를 만들어서 할 수도 있음.
        n = len(s)
        prefix_l_cnt = [0] * n
        prefix_t_cnt = [0] * n

        for i in range(n):
            if i - 1 >= 0:
                prefix_l_cnt[i] += prefix_l_cnt[i-1]
                prefix_t_cnt[i] += prefix_t_cnt[i-1]
            if s[i] == 'L':
                prefix_l_cnt[i] +=1
            elif s[i] == 'T':
                prefix_t_cnt[i] += 1

        def lct_count_with_extra() -> int:
            ret = 0
            extra_c_best = 0

            candidates = [0, 0, 0]

            for i in range(0, n):
                left_l = 0
                right_t = 0
                if i-1 >= 0:
                    left_l += prefix_l_cnt[i-1]
                right_t += prefix_t_cnt[n-1] - prefix_t_cnt[i]

                if s[i] == 'C':
                    candidates[0] += (left_l + 1) * right_t
                    candidates[1] += left_l * (right_t + 1)
                    candidates[2] += left_l * right_t
                    ret += left_l * right_t

                extra_c_best = max(extra_c_best, left_l *
                                   (prefix_t_cnt[n-1] - prefix_t_cnt[i-1]))
            candidates[2] += extra_c_best
            return max(candidates)

        return lct_count_with_extra()
