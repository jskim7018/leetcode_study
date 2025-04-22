
def main():
    t = int(input())

    for _ in range(t):
        n,m,k = map(int, input().split())

        grid = [[0] * m for _ in range(n)]

        if m % k != 0:
            val = 1
            for i in range(n):
                for j in range(m):
                    grid[i][j] = val
                    val += 1
                    if val > k:
                        val = 1
        else:
            for i in range(n):
                start = (k - i) % k + 1
                row = []
                val = start
                for j in range(m):
                    row.append(val)
                    val += 1
                    if val > k:
                        val = 1
                grid[i] = row

        for row in grid:
            print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()