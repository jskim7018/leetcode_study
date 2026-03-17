from typing import List


class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.children = [None] * 26


class Solution:
    def partitionString(self, s: str) -> List[str]:
        # rolling hash? Trie?

        trie_roots = [None] * 26

        curr_trie = trie_roots
        start_idx = 0
        ans = []
        for i, ch in enumerate(s):
            ch_idx = ord(ch) - ord('a')
            if curr_trie[ch_idx] is None:
                ans.append(s[start_idx:i+1])
                trie_node = TrieNode(ch)
                curr_trie[ch_idx] = trie_node
                curr_trie = trie_roots
                start_idx = i + 1
            else:
                curr_trie = curr_trie[ch_idx].children

        return ans
