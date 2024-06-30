class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.triangle_height(red,blue),
                   self.triangle_height(blue,red))

    def triangle_height(self, ball1: int, ball2: int) -> int:
        curr_h=0
        curr_phase = 1
        while True:
            need_ball1 = 1+(curr_phase-1)*2
            if ball1 >= need_ball1:
                ball1 -= need_ball1
                curr_h+=1
            else:
                break

            need_ball2 = (curr_phase)*2
            if ball2 >= need_ball2:
                ball2 -= need_ball2
                curr_h += 1
            else:
                break

            curr_phase += 1
        return curr_h
