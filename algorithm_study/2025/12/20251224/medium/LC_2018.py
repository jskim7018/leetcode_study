from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])

        word_len = len(word)

        def check_spot_and_word(curr_spot) -> bool:
            is_possible = True
            for i in range(word_len):
                if curr_spot[i] != ' ' and curr_spot[i] != word[i]:
                    is_possible = False
                    break
            if is_possible:
                return True

            is_possible = True
            for i in range(word_len):
                if curr_spot[i] != ' ' and curr_spot[i] != word[-i - 1]:
                    is_possible = False
                    break
            if is_possible:
                return True

            return False

        def check_board(is_horizontal: bool) -> bool:
            if is_horizontal:
                line_cnt = m
                block_cnt = n
            else:
                line_cnt = n
                block_cnt = m
            for i in range(line_cnt):
                curr_spot = []
                j = 0
                while j < block_cnt:
                    if board[i if is_horizontal else j][j if is_horizontal else i] != '#':
                        curr_spot.append(board[i if is_horizontal else j][j if is_horizontal else i])
                    if board[i if is_horizontal else j][j if is_horizontal else i] == '#' or j == block_cnt - 1:
                        if len(curr_spot) == word_len:
                            is_possible = check_spot_and_word(curr_spot)
                            if is_possible:
                                return True
                        curr_spot.clear()
                    j += 1
            return False
        check_board_hor = check_board(is_horizontal=True)
        check_board_vert = check_board(is_horizontal=False)

        return check_board_hor or check_board_vert
