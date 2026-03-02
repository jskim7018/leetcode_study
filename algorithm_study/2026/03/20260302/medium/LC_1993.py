from typing import List
from collections import defaultdict
# lock, unlock은 매우 쉬움.
# upgrade는 부모 및 자식 노드를 모두 확인해야함. 즉 사실상 그래프 순회를 통을 해야함.
# 시간 복잡도 상으로는 가능한데 더 나은 방법은 없을까?


class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = defaultdict(int)
        self.tree = defaultdict(list)
        for i in range(len(parent)):
            if parent[i] != -1:
                self.tree[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = user
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        if (num in self.locked and
                self.locked[num] == user):
            del self.locked[num]
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        curr = num
        while curr != -1:
            if curr in self.locked:
                return False
            curr = self.parent[curr]

        stck = [num]
        is_possible = False
        while stck:
            curr = stck.pop()
            for child in self.tree[curr]:
                if child in self.locked:
                    is_possible = True
                    del self.locked[child]
                stck.append(child)
        if is_possible:
            self.locked[num] = user
            return True
        return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)