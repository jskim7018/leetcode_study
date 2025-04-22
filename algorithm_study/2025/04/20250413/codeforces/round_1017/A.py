N = int(input())

for _ in range(N):
    lst = input().split()
    ans = ""
    for s in lst:
        ans += s[0]
    print(ans)