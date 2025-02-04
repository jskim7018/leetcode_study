from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = Counter(s)
        print(counter.most_common())

        mp_key_press_cnt = {}

        i = 0
        cnt = 1
        for c in counter.most_common():
            mp_key_press_cnt[c[0]] = cnt
            i+=1
            if i >= 9:
                i = 0
                cnt += 1

        ans = 0
        for c in s:
            ans += mp_key_press_cnt[c]
        return ans
