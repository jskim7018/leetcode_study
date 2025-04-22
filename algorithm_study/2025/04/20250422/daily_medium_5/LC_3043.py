from typing import List


class Node:
    def __init__(self):
        self.nexts = [None] * 10


class Trie:
    def __init__(self):
        self.nodes = [None] * 10
    def set(self, s: str):
        nodes = self.nodes
        for c in s:
            key = ord(c)-ord('0')
            if nodes[key] is None:
                nodes[key] = Node()
            nodes = nodes[key].nexts

    def get_lcs(self, s: str):
        cnt = 0
        nodes = self.nodes
        for c in s:
            key = ord(c)-ord('0')
            if nodes[key] is not None:
                nodes = nodes[key].nexts
                cnt += 1
            else:
                break
        return cnt

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for a in arr1:
            trie.set(str(a))

        ans = 0
        for a in arr2:
            ans = max(ans, trie.get_lcs(str(a)))

        return ans
