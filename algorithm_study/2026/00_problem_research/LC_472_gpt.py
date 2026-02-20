from typing import List

class Solution:
    # ✅ O(N · L²)
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        result = []

        for word in words:  # N
            word_set.remove(word)

            if self.can_form(word, word_set):  # L²
                result.append(word)

            word_set.add(word)

        return result

    def can_form(self, word: str, word_set: set) -> bool:
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True

        # TODO: total L의 길이가 10^5 인데 그럼 L^는 10^10이다. 그런데도 어떻게 시간안에 끝나지?
        for i in range(1, n + 1):  # L
            for j in range(i):  # L
                # 이전꺼를 다시 계산하는 것이 아니라 되는지 안되는지 True False만 계산해두면 됨.
                # 근데 word[j:i]도 L 시간 복잡도가 아닌가?
                if dp[j] and word[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
