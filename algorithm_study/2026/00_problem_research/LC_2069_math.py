class Robot:

    def __init__(self, width: int, height: int):
        self.W = width - 1
        self.H = height - 1
        self.P = 2 * (self.W + self.H)
        self.pos = 0
        self.hasMoved = False

    def step(self, num: int) -> None:
        self.hasMoved = True
        self.pos = (self.pos + num) % self.P

    def getPos(self) -> list:
        if self.pos <= self.W:
            return [self.pos, 0]
        if self.pos <= self.W + self.H:
            return [self.W, self.pos - self.W]
        if self.pos <= 2 * self.W + self.H:
            return [self.W - (self.pos - (self.W + self.H)), self.H]
        return [0, self.H - (self.pos - (2 * self.W + self.H))]

    def getDir(self) -> str:
        if not self.hasMoved:
            return "East"
        if self.pos == 0:
            return "South"
        if self.pos <= self.W:
            return "East"
        if self.pos <= self.W + self.H:
            return "North"
        if self.pos <= 2 * self.W + self.H:
            return "West"
        return "South"