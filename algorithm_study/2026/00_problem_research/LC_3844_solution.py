from collections import defaultdict


class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        # TODO: Study thoroughly: https://leetcode.com/problems/longest-almost-palindromic-substring/solutions/7582870/99-ms-in-python-powered-by-bitset-vector-7pyu/
        '''
        On the LeetCode solutions/discuss side, the common buckets for this kind of problem are:
        1. DP on intervals (O(n^2) time; O(n^2) space if kept full; can be rolled to O(n) space).
        2. Expand around center with one skip (two pointers with a “used deletion?” flag).
        3. Bitset acceleration: keep the same DP idea, but compress a whole DP “row” into a big integer and update it with >> & | (C-level operations in Python).
        This is the reason you can get ~100ms instead of seconds.
        '''
        # character -> bitmask of its positions
        char_positions = defaultdict(int)
        for idx, ch in enumerate(s):
            char_positions[ch] |= 1 << idx

        # Bitsets for substrings ending at previous index
        perfect_pal = 1        # length 1 base case
        almost_pal = 1         # length 1 is also almost-pal
        max_length = 2

        # Keeps valid left boundary bits
        valid_mask = 3
        base_shift = 3

        for right in range(1, n):

            # All left positions where s[left] == s[right]
            matching_lefts = char_positions[s[right]] & valid_mask

            # Build new perfect palindromes
            new_perfect = matching_lefts & ((perfect_pal >> 1) | base_shift)

            # Build new almost-palindromes
            new_almost = (
                (matching_lefts & ((almost_pal >> 1) | base_shift))  # extend previous almost
                | (new_perfect >> 1)                                 # mismatch used now
                | perfect_pal                                        # delete right char case
            ) & valid_mask

            # Find longest substring ending at 'right'
            leftmost_bit = (new_almost & -new_almost)
            if leftmost_bit:
                left_index = leftmost_bit.bit_length() - 1
                length = right - left_index + 1
                max_length = max(max_length, length)

            perfect_pal, almost_pal = new_perfect, new_almost
            valid_mask = (valid_mask << 1) | 1
            base_shift <<= 1

        return max_length
