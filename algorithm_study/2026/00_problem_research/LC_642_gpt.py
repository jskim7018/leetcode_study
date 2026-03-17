from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.counts = defaultdict(int)  # sentence -> frequency


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.curr_node = self.root
        self.curr_input = ""

        # Insert initial sentences
        for sentence, time in zip(sentences, times):
            self._insert(sentence, time)

    def _insert(self, sentence, time):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.counts[sentence] += time

    def input(self, c):
        if c == '#':
            # End of input, store sentence
            self._insert(self.curr_input, 1)
            self.curr_input = ""
            self.curr_node = self.root
            return []

        self.curr_input += c

        if self.curr_node:
            if c in self.curr_node.children:
                self.curr_node = self.curr_node.children[c]
            else:
                self.curr_node = None

        if not self.curr_node:
            return []

        # Get top 3 hot sentences
        sentences = list(self.curr_node.counts.items())
        sentences.sort(key=lambda x: (-x[1], x[0]))  # freq desc, ASCII asc
        return [s for s, _ in sentences[:3]]