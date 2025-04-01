from collections import Counter

N = int(input())

P = list(map(int, input().split()))
counter = Counter(P)

N_P = [[P[i], i,0] for i in range(N)]

N_P.sort(reverse=True)

rank = 1
for i in range(N):
    if i > 0:
        if N_P[i][0] != N_P[i-1][0]:
            rank += counter[N_P[i-1][0]]
    N_P[i][2] = rank

N_P.sort(key=lambda x:x[1])
ans = [np[2] for np in N_P]
for a in ans:
    print(a)