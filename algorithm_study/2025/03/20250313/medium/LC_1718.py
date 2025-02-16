from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:


        used = set()
        ans = []
        def construct(idx, seq) -> bool:
            nonlocal ans
            if idx >= len(seq):
                if -1 not in seq:
                    ans = list(seq)
                    return True
                else:
                    return False
            if seq[idx] != -1:
                return construct(idx+1, seq)
            else:
                for i in range(n, 0, -1):
                    if i not in used:
                        if (i != 1 and idx+i >= len(seq)) or (i != 1 and seq[idx+i] != -1):
                            continue
                        used.add(i)
                        seq[idx] = i
                        if i != 1:
                            seq[idx+i] = i
                        isFound = construct(idx+1, seq)
                        used.remove(i)
                        seq[idx] = -1
                        if i != 1:
                            seq[idx+i] = -1
                        if isFound:
                            return isFound
            return False

        seq = [-1] * (n * 2 - 1)
        construct(0, seq)
        return ans
