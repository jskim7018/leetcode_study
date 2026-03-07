import random


class RandomizedSet:

    def __init__(self):
        self.val_set = set()
        self.val_list = list()
        self.val_to_idx = dict()

    def insert(self, val: int) -> bool:
        if val not in self.val_set:
            self.val_set.add(val)
            self.val_list.append(val)
            self.val_to_idx[val] = len(self.val_list)-1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.val_set:
            self.val_set.remove(val)
            idx = self.val_to_idx[val]
            self.val_list[idx] = self.val_list[-1]
            self.val_to_idx[self.val_list[-1]] = idx
            self.val_list.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        n = len(self.val_list)

        idx = random.randint(0, n-1)

        return self.val_list[idx]
