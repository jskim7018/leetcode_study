def to_base(n: int, base: int) -> str:
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    is_negative = n < 0
    n = abs(n)

    while n:
        result.append(digits[n % base])
        n //= base

    if is_negative:
        result.append('-')

    return ''.join(reversed(result))
