# The time complexity of the Z-algorithm is O(n)
# version2 - (z[0] = 0)
def z_algorithm1(s: str) -> list[int]:
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

# version 2 - (z[0] = n)
def z_algorithm2(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    z[0] = n  # This is the only difference from first version

    l, r = 0, 0  # window [l, r]

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        # try to extend match
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # update window
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z