t = int(input())

for _ in range(t):
    N, K = map(int, input().split())

    A = list(map(int, input().split()))
    A.sort()
    left = ((len(A) - K))
    right = (K + len(A))
    if left % 2 == 0:
        left = (left//2)
        idx1 = left-1
        idx2 = left

        right = (right//2)
        ridx1 = right-1
        ridx2 = right
    else:
        left = (left // 2)
        idx1 = left
        idx2 = left

        right = (right // 2)
        ridx1 = right
        ridx2 = right
    minim = min(A[idx1], A[idx2], A[ridx1], A[ridx2])
    maxim = max(A[idx1], A[idx2], A[ridx1], A[ridx2])

    print(maxim-minim + 1)