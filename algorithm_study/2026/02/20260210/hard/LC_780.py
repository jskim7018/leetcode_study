class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # tx-sx = dx, ty-sy = dy. dx와 dy를 만들 수 있나?
        # if x wants to receive x, it needs to receive with y
        # operation의 갯수는 2가지 뿐. 순서 상관이 있나?
        # x, x+y -> x+x+y, x+y
        # x+y, y -> x+y, x+y+y
        # 어찌됐든 결국 하나는 완성해야 함.
        # 하나를 완성하면 다른 남은 하나는 완성된 걸로 완성해야 함
        # 무조건 작은것 부터 만들어야 함.
        # 아래 조건을 만족하는 것을 만들 수 있으면 가능
        # - 작은거를 완성할때 (큰거 - 작은거)가 작은거의 배수가 되어야 함.
        # TODO: 자세히 공부 필요.
        # TODO: 큰애가 될려면 작은애가 무조건 더해져야 한다.
        # TODO: 그러므로 큰애가 작은애보다 작아질때까지 작은애를 뺀다 => modulo로 빠르게 가능
        # 이것을 계속 반복한다.

        while tx > sx and ty > sy:
            if ty > tx:
                ty %= tx
            else:
                tx %= ty

        if tx == sx and ty == sy:
            return True
        if tx < sx or ty < sy:
            return False

        if tx == sx:
            if (ty-sy) % sx == 0:
                return True
            else:
                return False
        elif ty == sy:
            if (tx-sx) % sy == 0:
                return True
            else:
                return False
        else:
            return False
