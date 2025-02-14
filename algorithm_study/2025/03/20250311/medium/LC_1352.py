class ProductOfNumbers:

    def __init__(self):
        self.products = list()
        self.valid_size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.valid_size = 0
        else:
            self.valid_size += 1
        if len(self.products) == 0 or self.products[-1] == 0:
            self.products.append(num)
        else:
            self.products.append(num*self.products[-1])

    def getProduct(self, k: int) -> int:
        if self.valid_size < k:
            return 0

        if len(self.products)-k-1 < 0 or self.products[-k-1] == 0:
            return int(self.products[-1])
        else:
            return int(self.products[-1]/self.products[-k-1])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)