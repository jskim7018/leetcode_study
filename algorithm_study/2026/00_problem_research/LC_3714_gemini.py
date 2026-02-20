class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        self.ans = 0
        # TODO: need to study below thoroughly
        # Case 1: 1 distinct character (longest run of same char)
        if n > 0:
            streak = 1
            self.ans = 1
            for i in range(1, n):
                if s[i] == s[i - 1]:
                    streak += 1
                else:
                    streak = 1
                if streak > self.ans: self.ans = streak

        # Case 2: Exactly 2 characters
        # We split by the 'forbidden' char to ensure the chunk has AT MOST 2 types.
        for c1, c2, forbidden in [('a', 'b', 'c'), ('b', 'c', 'a'), ('a', 'c', 'b')]:
            for chunk in s.split(forbidden):
                if not chunk: continue

                # Prefix difference for two characters
                seen = {0: -1}
                cnt1 = cnt2 = 0
                for i, char in enumerate(chunk):
                    if char == c1:
                        cnt1 += 1
                    else:
                        cnt2 += 1

                    diff = cnt1 - cnt2
                    # Must have at least one of each to be "2 distinct characters"
                    if cnt1 > 0 and cnt2 > 0:
                        if diff in seen:
                            length = i - seen[diff]
                            if length > self.ans: self.ans = length

                    if diff not in seen:
                        seen[diff] = i

        # Case 3: Exactly 3 characters
        # Key: (count_a - count_b, count_b - count_c)
        seen = {(0, 0): -1}
        ca = cb = cc = 0
        for i, char in enumerate(s):
            if char == 'a':
                ca += 1
            elif char == 'b':
                cb += 1
            else:
                cc += 1

            diff = (ca - cb, cb - cc)
            # Must have at least one of each for "3 distinct characters"
            if ca > 0 and cb > 0 and cc > 0:
                if diff in seen:
                    length = i - seen[diff]
                    if length > self.ans: self.ans = length

            if diff not in seen:
                seen[diff] = i

        return self.ans