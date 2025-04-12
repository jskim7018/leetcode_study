def max_min_mex_optimized(n, k, arr):
    def can_make(x):
        seen = [0] * x
        unique = 0
        sets_formed = 0

        for num in arr:
            if num < x and seen[num] == 0:
                seen[num] = 1
                unique += 1
            if unique == x:
                sets_formed += 1
                seen = [0] * x
                unique = 0
            if sets_formed >= k:
                return True
        return False

    low, high = 0, n + 1
    while low < high:
        mid = (low + high) // 2
        if can_make(mid):
            low = mid + 1
        else:
            high = mid
    return low - 1

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_min_mex_optimized(n, k, arr))
