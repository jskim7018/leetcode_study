from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter_1 = Counter()
        counter_2 = Counter()
        for w in word1:
            counter_1[w] += 1
        for w in word2:
            counter_2[w] += 1

        return (sorted(counter_1.values()) == sorted(counter_2.values())
                and sorted(counter_1.keys()) == sorted(counter_2.keys()))

"""
Counter 인수에 지정해서 바로 카운트를 구할 수 있음. 직접 루프를 돌 필요 없음.

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        return sorted(c1.values()) == sorted(c2.values()) and sorted(c1.keys()) == sorted(c2.keys())
"""