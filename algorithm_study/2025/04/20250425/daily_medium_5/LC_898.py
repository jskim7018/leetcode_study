from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()     # all distinct OR‐results
        cur = set()     # OR‐results for subarrays ending at the previous index

        for x in arr:
            # start new OR‐set for ending at this index
            new_cur = {x}
            # extend all previous subarrays by x
            for v in cur:
                new_cur.add(v | x)

            # add to global results
            res |= new_cur

            # slide window: this becomes the "previous" for next iteration
            cur = new_cur

        return len(res)
