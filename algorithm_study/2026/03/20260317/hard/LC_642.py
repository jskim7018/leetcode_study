from typing import List
from collections import defaultdict
from sortedcontainers import SortedSet

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.hot_sentences = SortedSet()

# Trie? save 3 hot ones per each node.
# Sorted Set 사용. (3개까지)
class AutocompleteSystem:

    def _add_sentence(self, sentence: str, cnt: int):
        self.sentence_to_cnt[sentence] += cnt
        self._update_trie(sentence)

    def _update_trie(self, sentence: str):
        curr_trie = self.hot_trie

        for ch in sentence:
            if ch not in curr_trie:
                curr_trie[ch] = TrieNode(ch)
            bef = (-(self.sentence_to_cnt[sentence] - 1), sentence)
            if bef in curr_trie[ch].hot_sentences:
                curr_trie[ch].hot_sentences.remove(bef)
            curr_trie[ch].hot_sentences.add((-self.sentence_to_cnt[sentence], sentence))
            if len(curr_trie[ch].hot_sentences) > 3:
                curr_trie[ch].hot_sentences.pop()
            curr_trie = curr_trie[ch].children

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentence_to_cnt = defaultdict(int)
        self.hot_trie = dict()
        self.curr_trie = self.hot_trie
        self.curr_sentence = []
        for i, sentence in enumerate(sentences):
            self._add_sentence(sentence, times[i])

    def input(self, c: str) -> List[str]:
        if c == '#':
            self._add_sentence(''.join(self.curr_sentence), 1)
            self.curr_sentence.clear()
            self.curr_trie = self.hot_trie
            return []
        else:
            ret = []
            if c in self.curr_trie:
                ret = [sentence for _, sentence in self.curr_trie[c].hot_sentences]
                self.curr_trie = self.curr_trie[c].children
            else:
                self.curr_trie = dict()
            self.curr_sentence.append(c)
            return ret

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)