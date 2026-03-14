class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        minim_idx = -1
        minim = float('inf')
        for i in range(len(capacity)):
            if itemSize <= capacity[i]:
                if minim > capacity[i]:
                    minim = capacity[i]
                    minim_idx = i
        return minim_idx
