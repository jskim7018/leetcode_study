from typing import List
from collections import defaultdict


# TODO: 각, cell 별로 sum의 위치를 저장해서 할 수 있음. 그러면 cell이 바뀌면 해당 sum들을 바로 update/propagate 가능.
class Excel:

    def __init__(self, height: int, width: str):
        col_num = self._col_number(width)
        self.grid = [[0] * (col_num+1) for _ in range(height+1)]
        self.sum_rects = defaultdict(list)

    def _col_number(self, width: str):
        return ord(width) - ord('A')

    def _update_cell(self, row: int, col_num: int, new_val: int):
        old_val = self.grid[row][col_num]
        self.grid[row][col_num] = new_val
        for k, v in self.sum_rects.items():
            for top, bot in v:
                if top[0] <= row <= bot[0] and top[1] <= col_num <= bot[1]:
                    self._update_cell(k[0], k[1], self.grid[k[0]][k[1]] - old_val + new_val)

    # set이 핵심. set에서 변경 일어나면 현재 set된게 포함되는 모든 sum을 갱신.
    # 갱신하고 나서 해당 갱신 된 것으로도 확인해야 함. queue를 활용하면 될듯.
    def set(self, row: int, column: str, val: int) -> None:
        col_num = self._col_number(column)
        if (row, col_num) in self.sum_rects:
            del self.sum_rects[(row, col_num)]
        self._update_cell(row, col_num, val)

    def get(self, row: int, column: str) -> int:
        col_num = self._col_number(column)
        return self.grid[row][col_num]

    # 여기도 갱신 해줘야 할 수 있음. set이랑 같음.
    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        col_num = self._col_number(column)
        if (row, col_num) in self.sum_rects:
            del self.sum_rects[(row, col_num)]

        sum_rect_list = []
        _sum = 0
        for rect in numbers:
            if ":" in rect:
                top, bot = rect.split(":")
                top_r, top_c = int(top[1:]), self._col_number(top[0])
                bot_r, bot_c = int(bot[1:]), self._col_number(bot[0])
            else:
                top_r, top_c = int(rect[1:]), self._col_number(rect[0])
                bot_r, bot_c = top_r, top_c
            sum_rect_list.append(((top_r, top_c), (bot_r, bot_c)))

            for i in range(top_r, bot_r+1):
                for j in range(top_c, bot_c+1):
                    _sum += self.grid[i][j]
        self._update_cell(row, col_num, _sum)
        self.sum_rects[(row, col_num)] = sum_rect_list
        return self.grid[row][col_num]
