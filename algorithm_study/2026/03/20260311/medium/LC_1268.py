from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.top_words = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Trie 사용.
        # 각, Trie Node 별로 최대 3개 저장.
        # 정렬 후 하면 그리디로 저장 가능.
        # time complexity: O(n*m*3) -> O(n*m)
        trie_roots = [None] * 26
        products.sort()

        for p in products:
            if p[0] != searchWord[0]:
                continue
            curr_node = trie_roots
            for ch in p:
                idx = ord(ch) - ord('a')
                if curr_node[idx] is None:
                    curr_node[idx] = TrieNode()
                if len(curr_node[idx].top_words) < 3:
                    curr_node[idx].top_words.append(p)
                curr_node = curr_node[idx].children

        ans = []
        curr_node = trie_roots
        for ch in searchWord:
            idx = ord(ch) - ord('a')
            if curr_node is not None and curr_node[idx] is not None:
                ans.append(curr_node[idx].top_words)
                curr_node = curr_node[idx].children
            else:
                ans.append([])
                curr_node = None

        return ans
