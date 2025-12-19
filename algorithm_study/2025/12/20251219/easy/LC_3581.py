from collections import Counter


class Solution:
    def countOddLetters(self, n: int) -> int:
        digit_words = ['zero', 'one', 'two', 'three', 'four', 'five',
                       'six', 'seven', 'eight', 'nine']

        counter = Counter()
        while n > 0:
            counter += Counter(digit_words[n%10])
            n //= 10

        ans = 0
        for v in counter.values():
            if v % 2==1:
                ans += 1

        return ans

# from collections import Counter
#
# class Solution:
#     def countOddLetters(self, n: int) -> int:
#         words = [
#             "zero", "one", "two", "three", "four",
#             "five", "six", "seven", "eight", "nine"
#         ]
#
#         s = "".join(words[int(d)] for d in str(n))
#         freq = Counter(s)
#
#         return sum(1 for c in freq.values() if c % 2 == 1)