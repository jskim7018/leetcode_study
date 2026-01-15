from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.n and 1 <= account2 <= self.n:
            if self.balance[account1-1] < money:
                return False

            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n:
            self.balance[account-1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n:
            if self.balance[account-1] < money:
                return False

            self.balance[account-1] -= money
            return True
        else:
            return False