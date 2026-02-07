# The time complexity of building the LPS array is O(n)
def compute_lps(pattern: str):
    n = len(pattern)
    lps = [0] * n

    length = 0  # length of previous longest prefix suffix
    i = 1

    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # fallback
            else:
                lps[i] = 0
                i += 1

    return lps