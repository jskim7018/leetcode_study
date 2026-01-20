class DataStream:

    def __init__(self, value: int, k: int):
        self.eq_cnt = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.eq_cnt += 1
        else:
            self.eq_cnt = 0
        if self.eq_cnt >= self.k:
            return True
        else:
            return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)