class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:

        curr_apples = 0
        i = 1

        x_accum = 0
        while curr_apples < neededApples:
            x_accum += ((i-1)*2) * 4
            curr_apples += (i*2*4) + (((i*2)-1) * i) * 4 + x_accum
            i += 1

        side_len = (i-1)*2
        return side_len * 4
