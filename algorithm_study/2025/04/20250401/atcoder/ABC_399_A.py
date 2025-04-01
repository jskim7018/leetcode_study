n = int(input())

S = input()
T = input()

ans = 0

for i in range(n):
    if S[i] != T[i]:
        ans += 1
print(ans)