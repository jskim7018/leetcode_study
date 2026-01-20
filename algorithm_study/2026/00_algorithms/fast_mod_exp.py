
# iterative (recommended) - For b = 10^9, this runs in ~30 steps.
def mod_pow(a: int, b: int, m: int) -> int:
    result = 1
    a %= m

    while b > 0:
        if b & 1:              # if b is odd
            result = (result * a) % m
        a = (a * a) % m        # square the base
        b >>= 1                # b = b // 2

    return result

# recursive - For b = 10^9, this runs in ~30 steps.
def mod_pow(a: int, b: int, m: int) -> int:
    if b == 0:
        return 1 % m

    half = mod_pow(a, b // 2, m)
    half = (half * half) % m

    if b % 2 == 0:
        return half
    else:
        return (half * a) % m