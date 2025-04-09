N = int(input())


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


for _ in range(N):
    x, k = map(int, input().split())
    if x == 1 and k == 2:
        print("YES")
    elif k >= 2:
        print("NO")
    else:
        if is_prime(x):
            print("YES")
        else:
            print("NO")