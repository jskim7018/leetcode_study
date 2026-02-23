import heapq


class StockPrice:
    # heap + lazy deletion
    def __init__(self):
        self.time_to_price = dict()
        self.max_heap = []  # -price, timestamp
        self.min_heap = []  # price, timestamp => TODO 변수 하나로 대체 가능. (latest time)
        self.time_min = []  # -timestamp, price

    def update(self, timestamp: int, price: int) -> None:
        self.time_to_price[timestamp] = price
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.time_min, (-timestamp, price))

    def current(self) -> int:
        while self.time_min and self.time_to_price[-self.time_min[0][0]] != self.time_min[0][1]:
            heapq.heappop(self.time_min)
        return self.time_min[0][1]

    def maximum(self) -> int:
        while self.max_heap and self.time_to_price[self.max_heap[0][1]] != -self.max_heap[0][0]:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def minimum(self) -> int:
        while self.min_heap and self.time_to_price[self.min_heap[0][1]] != self.min_heap[0][0]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

def test_StockPrice():
    stock_price = StockPrice()

    stock_price.update(1, 10)
    stock_price.update(2, 5)
    assert stock_price.current() == 5
    assert stock_price.maximum() == 10
    stock_price.update(1, 3)
    assert stock_price.maximum() == 5
    stock_price.update(4, 2)
    assert stock_price.minimum() == 2
    stock_price.update(4, 3)
    assert stock_price.minimum() == 3

