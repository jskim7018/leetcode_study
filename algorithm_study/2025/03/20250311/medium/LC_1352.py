class ProductOfNumbers:

    def __init__(self):
        self.products = list()
        self.zero_cnt = []

    def add(self, num: int) -> None:
        if len(self.zero_cnt) == 0:
            self.zero_cnt.append((num == 0))
        else:
            self.zero_cnt.append(self.zero_cnt[-1]+(num == 0))
        if len(self.products) == 0 or self.products[-1] == 0:
            self.products.append(num)
        else:
            self.products.append(num*self.products[-1])

    def getProduct(self, k: int) -> int:
        zeros = self.zero_cnt[-1]
        if len(self.zero_cnt)-k-1 >= 0:
            zeros -= self.zero_cnt[-k-1]
        if zeros > 0:
            return 0

        if len(self.products)-k-1 < 0 or self.products[-k-1] == 0:
            return int(self.products[-1])
        else:
            return int(self.products[-1]/self.products[-k-1])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)