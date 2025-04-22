import heapq
import math
from functools import cache

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    bigger_cnt = 0
    smaller_cnt = 0
    work_cnt = 0
    # check left and right
    left_idx = -1
    for i in range(n):
        if A[i] > k:
            bigger_cnt += 1
        else:
            smaller_cnt += 1

        if smaller_cnt != 0 and smaller_cnt >= bigger_cnt:
            left_idx = i
            break
    right_idx = -1
    bigger_cnt = 0
    smaller_cnt = 0
    for i in range(n):
        if A[n-i-1] > k:
            bigger_cnt += 1
        else:
            smaller_cnt += 1

        if smaller_cnt != 0 and smaller_cnt >= bigger_cnt:
            right_idx = n-i-1
            break
    if left_idx + 1 < right_idx and left_idx != -1 and right_idx != -1:
        print("YES")
    else:
        def check_left_middle() -> bool:
            cnt = 0
            left_idx = -1
            bigger_cnt = 0
            smaller_cnt = 0
            i = 0
            # check left, middle
            while i < n:
                if A[i] > k:
                    bigger_cnt += 1
                else:
                    smaller_cnt += 1

                if smaller_cnt > 0 and smaller_cnt >= bigger_cnt:
                    cnt += 1
                    if cnt == 1 and i + 1 < n and A[i + 1] > k and smaller_cnt > bigger_cnt:
                        i += 1
                    smaller_cnt = 0
                    bigger_cnt = 0
                    if cnt >= 2:
                        left_idx = i
                i += 1
            if (left_idx < n - 1 and left_idx != -1):
                return True
            else:
                return False

        if check_left_middle():
            print("YES")
        else:
            A.reverse()
            if check_left_middle():
                print("YES")
            else:
                print("NO")