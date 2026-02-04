from typing import List
from collections import defaultdict


class Solution:
    def longestWord(self, words: List[str]) -> str:
        # 이전 상태와 다음 상태가 명확함. DP/frequency prefix 가능.
        words.sort(key=len) # TODO: 길이로 정렬하는것을 잊었는데 정렬 기준 명확히 하자.
        words_dict = defaultdict(bool)
        words_dict[""] = True

        ans = ""
        for word in words:
            if words_dict[word[:-1]]:
                words_dict[word] = True
                if len(word) > len(ans) or word < ans:
                    ans = word
        return ans
