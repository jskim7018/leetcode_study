from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)

        same_min = 0
        diff_cnt = 0
        total_same = 0
        is_odd_exist = False
        for word in counter.keys():
            if counter[word] != 0:
                if word[0] == word[1] and word in counter:
                    same_min = min(same_min, counter[word])
                    total_same += counter[word] - counter[word]%2
                    if counter[word] % 2:
                        is_odd_exist = True
                    counter[word] = 0
                elif counter[word[1]+word[0]] != 0:
                    minim = min(counter[word[1] + word[0]], counter[word])
                    diff_cnt += minim * 2
                    counter[word[1] + word[0]] = 0
                    counter[word] = 0
        if is_odd_exist:
            total_same += 1
        ans = 2 * (diff_cnt + total_same)
        return ans
