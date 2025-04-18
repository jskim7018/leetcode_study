def fast_mod_exp(base: int, exponent: int, mod: int) -> int:
    result = 1
    base = base % mod

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2

    return result

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
