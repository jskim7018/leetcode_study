from collections import Counter


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        def atleast_k(k_):
            vowels = set('aeiou')
            counter = Counter()
            l = 0
            curr_k = 0
            ret = 0
            for r in range(n):
                if word[r] in vowels:
                    counter[word[r]] += 1
                else:
                    curr_k += 1

                while len(counter) == 5 and curr_k >= k_:
                    ret += n-r
                    if word[l] in vowels:
                        counter[word[l]] -= 1
                        if counter[word[l]] == 0:
                            counter.pop(word[l])
                    else:
                        curr_k -= 1

                    l += 1
            return ret

        return atleast_k(k) - atleast_k(k+1)
