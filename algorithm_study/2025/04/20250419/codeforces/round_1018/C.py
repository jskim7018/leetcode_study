def main():
    INF = 10**30

    t = int(input())
    for _ in range(t):
        n = int(input())
        h = [list(map(int, input().split())) for _ in range(n)]
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        # Build allowed transitions for columns: allowed_c[j][u][v] means
        # we can have c_j = u and c_{j+1} = v (u,v in {0,1}).
        allowed_c = [[[True]*2 for _ in range(2)] for _ in range(n-1)]
        for j in range(n-1):
            M = allowed_c[j]
            for i in range(n):
                d = h[i][j] - h[i][j+1]
                if d == 0:
                    # forbid v-u == 0  ⇒ u=v
                    M[0][0] = False
                    M[1][1] = False
                elif d == 1:
                    # forbid v-u == 1 ⇒ (u,v) = (0,1)
                    M[0][1] = False
                elif d == -1:
                    # forbid v-u == -1 ⇒ (u,v) = (1,0)
                    M[1][0] = False

        # Build allowed transitions for rows: allowed_r[i][u][v] for r_i=u, r_{i+1}=v
        allowed_r = [[[True]*2 for _ in range(2)] for _ in range(n-1)]
        for i in range(n-1):
            M = allowed_r[i]
            for j in range(n):
                d = h[i][j] - h[i+1][j]
                if d == 0:
                    M[0][0] = False
                    M[1][1] = False
                elif d == 1:
                    M[0][1] = False
                elif d == -1:
                    M[1][0] = False

        # 1D DP along the columns for c[0..n-1] with cost B[j]*c[j]
        dp0, dp1 = 0.0, B[0]  # dp0 = cost if c0=0, dp1 = cost if c0=1
        ok_c = True
        for j in range(1, n):
            M = allowed_c[j-1]
            nd0 = INF
            nd1 = INF
            # transition into c_j = 0
            if M[0][0]:
                nd0 = min(nd0, dp0)
            if M[1][0]:
                nd0 = min(nd0, dp1)
            # transition into c_j = 1 (pay B[j])
            if M[0][1]:
                nd1 = min(nd1, dp0 + B[j])
            if M[1][1]:
                nd1 = min(nd1, dp1 + B[j])

            if nd0 >= INF and nd1 >= INF:
                ok_c = False
                break
            dp0, dp1 = nd0, nd1

        if not ok_c:
            print(-1)
            continue
        best_c = min(dp0, dp1)

        # 1D DP along the rows for r[0..n-1] with cost A[i]*r[i]
        dp0, dp1 = 0.0, A[0]
        ok_r = True
        for i in range(1, n):
            M = allowed_r[i-1]
            nd0 = INF
            nd1 = INF
            if M[0][0]:
                nd0 = min(nd0, dp0)
            if M[1][0]:
                nd0 = min(nd0, dp1)
            if M[0][1]:
                nd1 = min(nd1, dp0 + A[i])
            if M[1][1]:
                nd1 = min(nd1, dp1 + A[i])

            if nd0 >= INF and nd1 >= INF:
                ok_r = False
                break
            dp0, dp1 = nd0, nd1

        if not ok_r:
            print(-1)
            continue
        best_r = min(dp0, dp1)

        # Both independent, so total cost is sum
        # Round to int in case of tiny float errors
        total = best_c + best_r
        print(int(round(total)))


if __name__ == "__main__":
    main()
