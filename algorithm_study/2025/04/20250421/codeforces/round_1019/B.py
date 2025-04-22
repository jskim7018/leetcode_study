t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = 0
    curr_zero = True
    how_many_ones = 0
    how_many_zeroes = 0
    for c in s:
        if c == '1':
            if curr_zero:
                how_many_ones += 1
                ans += 1
                curr_zero=False
            ans += 1
        else:
            if not curr_zero:
                how_many_zeroes += 1
                ans += 1
                curr_zero = True
            ans += 1
    if how_many_zeroes > 0:
        if how_many_ones == 1:
            ans -= 1
        elif how_many_ones > 1:
            ans -= 2
    print(ans)
