N = int(input())

logged_in = False
ans = 0
for _ in range(N):
    S = input()
    if S == 'login':
        logged_in = True
    elif S == 'logout':
        logged_in = False
    elif S == 'private':
        if not logged_in:
            ans += 1
print(ans)