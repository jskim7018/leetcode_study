from typing import List


class Robot:
    # flatten?
    def __init__(self, width: int, height: int):
        self.flattened_positions = []
        for i in range(width):
            self.flattened_positions.append([i, 0, "East"])
        for i in range(1, height):
            self.flattened_positions.append([width-1, i, "North"])
        for i in range(width-2,-1,-1):
            self.flattened_positions.append([i, height-1, "West"])
        for i in range(height-2, 0, -1):
            self.flattened_positions.append([0, i, "South"])
        self.flattened_positions[0][2] = "South"
        self.is_moved = False
        self.steps_curr = 0

    def step(self, num: int) -> None:
        if num > 0:
            self.is_moved = True
        self.steps_curr = (self.steps_curr + num) % len(self.flattened_positions)

    def getPos(self) -> List[int]:
        return self.flattened_positions[self.steps_curr][:2]

    def getDir(self) -> str:
        if self.is_moved:
            return self.flattened_positions[self.steps_curr][2]
        else:
            return "East"

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()