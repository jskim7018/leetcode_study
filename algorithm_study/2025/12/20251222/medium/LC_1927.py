class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        left_q_cnt = 0
        right_q_cnt = 0
        left_num = 0
        right_num= 0

        for i in range(n // 2):
            if num[i] == '?':
                left_q_cnt += 1
            else:
                left_num += int(num[i])
        for i in range(n // 2, n):
            if num[i] == '?':
                right_q_cnt += 1
            else:
                right_num += int(num[i])

        if left_num == right_num and left_q_cnt == right_q_cnt:
            return False

        if left_num > right_num:
            num = left_num - right_num
            right_q_left = right_q_cnt - left_q_cnt

            if right_q_left % 2 == 0 and right_q_left != 0 and num/(right_q_left//2) == 9:
                return False
        elif left_num < right_num:
            num = right_num - left_num
            left_q_left = left_q_cnt - right_q_cnt
            if left_q_left % 2 == 0 and left_q_left != 0 and num/(left_q_left//2) == 9:
                return False
        return True
