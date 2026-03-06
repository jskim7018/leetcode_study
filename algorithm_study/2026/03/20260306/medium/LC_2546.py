class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # 1, 0 일때 -> 1 1 -> 0 1, 1 0
        # 1, 1 일때 -> 1 0, 0 1
        # 0, 0 일때 -> 0 0
        # 0, 1 일떄 -> 1 1
        # 0만 있을때는 1이 생겨 날 수 없음. 하지만 1이 여러개 일때는 1의 갯수(0이상)와 위치가 자유롭게 조정 가능.
        if s == target or s.count('1') > 0 and target.count('1') > 0:
            return True
        else:
            return False
