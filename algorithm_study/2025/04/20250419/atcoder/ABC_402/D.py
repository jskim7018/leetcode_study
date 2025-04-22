from collections import defaultdict

N, M = map(int, input().split())

mp = defaultdict(int)

for _ in range(M):
    A, B = map(int,input().split())
    mp[(A+B)%N] += 1

sum_ = 0
for v in mp.values():
    sum_ += v

ans = 0
for v in mp.values():
    sum_ -= v
    ans += sum_*v
print(ans)
