# The time complexity of building the LPS array is O(n)
def compute_lps(pattern: str):
    n = len(pattern)
    lps = [0] * n

    length = 0  # length of previous longest prefix suffix
    i = 1

    while i < n:
        # This is just moving left and right fingers to right. when found match.
        if pattern[i] == pattern[length]:
            length += 1  # left finger
            lps[i] = length
            i += 1  # right finger
        else:
            # lps 알고리즘에서 어려운 부분. fallback 할때 현재 prefix에서 가능한 가장 뒤쪽으로.
            if length != 0:
                length = lps[length - 1]  # fallback
            else:

                lps[i] = 0
                i += 1

    return lps