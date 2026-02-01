from typing import List


class TrieNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = dict()


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie_roots = TrieNode()

        for word in words:
            curr_trie = trie_roots
            for ch in word:
                if ch not in curr_trie.next:
                    curr_trie.next[ch] = TrieNode()
                curr_trie.next[ch].val += 1
                curr_trie = curr_trie.next[ch]

        ans = []
        for word in words:
            curr_trie = trie_roots
            curr_ans = 0
            for ch in word:
                curr_ans += curr_trie.next[ch].val
                curr_trie = curr_trie.next[ch]
            ans.append(curr_ans)

        return ans
