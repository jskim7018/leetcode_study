N, K = map(int, input().split())
MOD = int(1e9)
ans = []
sum_ = 0
for i in range(K):
    ans.append(1)
    sum_ += 1

answer = 1
for i in range(K, N+1):
    ans.append(sum_)
    sum_ -= ans[i-K]
    answer = sum_
    sum_ += ans[-1]
    sum_ %= MOD
print(ans[N])