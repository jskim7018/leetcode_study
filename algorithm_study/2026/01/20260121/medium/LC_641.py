class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

# TODO: list 방식도 고려했어야 했음. 가능한 모든 경우를 생각하고 trade-off를 얘기할 수 있어야 함.
# TODO: 나중에 list 방식도 구현해보자.
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value,nxt=self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        self.size += 1
        if self.tail is None:
            self.tail = node
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value, prev=self.tail)
        if self.tail is not None:
            self.tail.nxt = node
        self.tail = node
        self.size += 1
        if self.head is None:
            self.head = node
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return True
        self.head = self.head.nxt
        self.head.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return True

        self.tail = self.tail.prev
        self.tail.nxt = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.head is not None:
            return self.head.val
        else:
            return -1

    def getRear(self) -> int:
        if self.tail is not None:
            return self.tail.val
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()