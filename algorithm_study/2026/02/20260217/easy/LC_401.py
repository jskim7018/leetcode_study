from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # bit permutation 특정 갯수로 (중복 없이?)
        # TODO: 반대로 가능한 것들만 (hour < 12 minute < 60 모두 조합해서 해볼 수 있음) 약 (O(720))
        # TODO: - combinations로 [1,2,4,..] 리스트를 반들고 comb를 돌렸었도 됐음.
        combs = []

        def combinations(idx: int, curr: int):
            left = 10 - idx
            need = turnedOn - curr.bit_count()
            if need == 0:
                combs.append(curr)
                return
            elif left == need:
                mask = 2**need - 1
                combs.append(curr | mask)
                return

            combinations(idx + 1, curr)
            combinations(idx + 1, curr | (1 << (9-idx)))
        combinations(0, 0)

        ans = []
        for bitmask in combs:
            idx = 0
            hours = 0
            minutes = 0
            while bitmask > 0:
                if bitmask % 2:
                    if idx <= 5:
                        minutes += 2 ** idx
                    else:
                        hours += 2 ** (idx-6)
                idx += 1
                bitmask //= 2
            if hours < 12 and minutes < 60:
                ans.append(str(hours) + ":" + str(minutes).zfill(2))

        return ans
