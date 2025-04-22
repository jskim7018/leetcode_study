T = int(input())

def fast_pow(base: float, exponent: int) -> float:
    result = 1.0
    is_negative = exponent < 0
    exponent = abs(exponent)

    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2

    return 1 / result if is_negative else result

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    maxim = max(arr)
    bit_len = len(bin(maxim)[2:])
    bits = [0] * bit_len
    for a in arr:
        for i in range(bit_len):
            if (a >> i & 1) == 1:
                bits[i] += 1
    len_arr = len(arr)
    maxim_points = 0
    maxim_a = arr[0]
    for a in arr:
        points = 0
        for i in range(bit_len):
            if (a >> i & 1) == 1:
                points += (len_arr - bits[i]) * fast_pow(2, i)
            else:
                points += bits[i] * fast_pow(2, i)
        if points > maxim_points:
            maxim_a = a
            maxim_points = points
    ans = 0
    for a in arr:
        ans += maxim_a ^ a
    print(ans)