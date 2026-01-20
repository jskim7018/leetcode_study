class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowel_st = set("aeiou")
        # TODO optimize 해보기
        n = len(s)
        vowel_cnt_prefix_sum = [0] * n
        for i in range(n):
            if s[i] in vowel_st:
                vowel_cnt_prefix_sum[i] += 1
            if i-1 >=0:
                vowel_cnt_prefix_sum[i] += vowel_cnt_prefix_sum[i-1]

        ans = 0
        for i in range(n):
            vowels = vowel_cnt_prefix_sum[n - 1]
            if i - 1 >= 0:
                vowels -= vowel_cnt_prefix_sum[i - 1]
            consonants = n - i - vowels
            for j in range(n-1, i, -1):
                if vowels * consonants < k:
                    break
                if (vowels == consonants and
                        (vowels * consonants) % k == 0):
                    ans += 1
                if s[j] in vowel_st:
                    vowels -= 1
                else:
                    consonants -= 1
        return ans
