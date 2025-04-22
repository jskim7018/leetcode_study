T = int(input())

for _ in range(T):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    ans = [0] * 2*N
    for i in range(N):
        for j in range(N):
            ans[i+j+1] = grid[i][j]
    sorted_ans = sorted(ans)
    for i in range(len(sorted_ans) + 1):
        if i >= len(sorted_ans) or i != sorted_ans[i]:
            ans[0] = i
            break

    for a in ans:
        print(a, end=" ")
    print()
