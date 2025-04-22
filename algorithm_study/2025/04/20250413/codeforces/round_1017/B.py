T = int(input())

for _ in range(T):
    n,m,l,r = map(int, input().split())

    diff = n-m
    sub = min(-l, diff)
    l += sub
    diff -= sub
    if diff != 0:
        r -= diff

    print(f'{l} {r}')