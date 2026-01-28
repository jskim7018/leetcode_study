from typing import List
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # a가 b의 predecessor 판단법
        # 1. a is subsequence of b
        # 1. len(a)+1 == len(b)
        # directed graph를 만들고 traverse해서 가장 깊이 가는것이 정답. 이떄 dp로 캐시화 함.
        # TODO: dp 방식 확실히 이해하기 O(n x L^2) - 일종의 frequency 방식.
        # TODO: 이전의 것만 보면 되기에 이전 것들의 frequencyfmf 저장해둔다.

        words.sort(key=lambda x: len(x))
        dp = defaultdict(int)
        ans = 1
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                pred_cand = word[:i] + word[i+1:]
                dp[word] = max(dp[word], dp[pred_cand] + 1)
            ans = max(ans, dp[word])
        return ans
