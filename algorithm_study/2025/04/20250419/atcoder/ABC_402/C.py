from collections import defaultdict


N, M = map(int, input().split())

ingredients = []
for i in range(M):
    input1 = list(map(int, input().split()))
    ingredients.append(list(input1[1:]))

B = list(map(int, input().split()))

mp = defaultdict(int)
for i in range(len(B)):
    mp[B[i]] = i+1

ans = defaultdict(int)

for i in range(len(ingredients)):
    maxim = 0

    for j in range(len(ingredients[i])):
        maxim = max(maxim, mp[ingredients[i][j]])
    ans[maxim] += 1

for i in range(1,N+1):
    ans[i] += ans[i-1]
    print(ans[i])