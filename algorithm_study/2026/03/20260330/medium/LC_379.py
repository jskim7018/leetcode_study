class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.open_slots = set((range(maxNumbers)))

    def get(self) -> int:
        if self.open_slots:
            return self.open_slots.pop()
        else:
            return -1

    def check(self, number: int) -> bool:
        if number in self.open_slots:
            return True
        else:
            return False

    def release(self, number: int) -> None:
        self.open_slots.add(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)