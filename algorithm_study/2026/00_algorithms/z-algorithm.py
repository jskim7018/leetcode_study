# The time complexity of the Z-algorithm is O(n)
def z_algorithm(s: str):
    n = len(s)
    Z = [0] * n
    L = R = 0

    for i in range(1, n):
        if i <= R:
            Z[i] = min(R - i + 1, Z[i - L])

        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1

        if i + Z[i] - 1 > R:
            L, R = i, i + Z[i] - 1

    return Z