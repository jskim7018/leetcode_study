class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)

        # lps > z-algorithm > rolling hash -> 모두 가능 하지만 이런 순서로 더 좋음.
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
        lps = compute_lps(s)

        return s[:lps[n-1]]
