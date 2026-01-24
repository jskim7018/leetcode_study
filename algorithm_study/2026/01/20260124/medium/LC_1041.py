class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir_y = [1,0,-1,0]
        dir_x = [0,-1,0,1]
        dir = 0
        pos_y = 0
        pos_x = 0

        for instruction in instructions:
            if instruction == 'L':
                dir = (4 + (dir - 1)) % 4
            elif instruction == 'R':
                dir = (dir + 1) % 4
            else:
                pos_y += dir_y[dir]
                pos_x += dir_x[dir]

        if dir != 0 or (pos_y == 0 and pos_x == 0):
            return True
        else:
            return False
