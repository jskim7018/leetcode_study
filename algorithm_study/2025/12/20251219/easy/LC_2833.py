class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt_underscore = 0

        curr = 0
        for move in moves:
            if move == 'L':
                curr -= 1
            elif move == 'R':
                curr += 1
            else:
                cnt_underscore += 1

        return abs(curr) + cnt_underscore
