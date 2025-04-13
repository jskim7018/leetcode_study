def fast_mod_exp(base: int, exponent: int, mod: int) -> int:
    result = 1
    base = base % mod

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2

    return result