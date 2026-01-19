from sortedcontainers import SortedList
from collections import defaultdict


class AuctionSystem:

    def __init__(self):
        self.item_to_high_bid = defaultdict(lambda:SortedList(key=lambda x: (-x[0], -x[1])))
        self.item_to_curr_bid = defaultdict(lambda:defaultdict(int))

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if userId in self.item_to_curr_bid[itemId]:
            self.updateBid(userId, itemId, bidAmount)
        else:
            self.item_to_curr_bid[itemId][userId] = bidAmount
            self.item_to_high_bid[itemId].add((bidAmount,userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        prev_bidAmount = self.item_to_curr_bid[itemId][userId]
        self.item_to_high_bid[itemId].remove((prev_bidAmount, userId))
        self.item_to_high_bid[itemId].add((newAmount, userId))
        self.item_to_curr_bid[itemId][userId] = newAmount

    def removeBid(self, userId: int, itemId: int) -> None:
        currBid = self.item_to_curr_bid[itemId][userId]
        del self.item_to_curr_bid[itemId][userId]
        self.item_to_high_bid[itemId].remove((currBid, userId))

    def getHighestBidder(self, itemId: int) -> int:
        if self.item_to_high_bid[itemId]:
            return self.item_to_high_bid[itemId][0][1]
        else:
            return -1

# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)