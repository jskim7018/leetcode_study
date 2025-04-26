from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    counter = defaultdict(int)
    is_possible = False
    for a in A:
        counter[a] += 1
        if counter[a] >= 4:
            is_possible = True
            break

    A.sort()
    A.append(float('inf'))
    counter_2 = defaultdict(int)
    count_twos = 0
    for i in range(0, len(A)):
        if i == 0 or A[i] == A[i - 1] or A[i] == A[i - 1] + 1:
            counter_2[A[i]] += 1
            if counter_2[A[i]] == 2:
                count_twos += 1
                if count_twos >= 2:
                    is_possible = True
                    break
        else:
            if count_twos >= 2:
                is_possible = True
                break
            counter_2[A[i]] = 1
            count_twos = 0

    if is_possible:
        print("Yes")
    else:
        print("No")