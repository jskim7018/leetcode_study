from collections import deque


class AhoCorasick:
    def __init__(self):
        self.trie = [{}]
        self.fail = [0]
        self.output = [set()]

    def add_word(self, word, idx):
        node = 0
        for char in word:
            if char not in self.trie[node]:
                self.trie[node][char] = len(self.trie)
                self.trie.append({})
                self.fail.append(0)
                self.output.append(set())
            node = self.trie[node][char]

        self.output[node].add(idx)

    def build(self):
        queue = deque()

        for char, nxt in self.trie[0].items():
            queue.append(nxt)

        while queue:
            r = queue.popleft()

            for char, nxt in self.trie[r].items():
                queue.append(nxt)

                f = self.fail[r]
                while f and char not in self.trie[f]:
                    f = self.fail[f]

                self.fail[nxt] = self.trie[f].get(char, 0)
                self.output[nxt] |= self.output[self.fail[nxt]]

    def search(self, text, patterns):
        node = 0
        result = []

        for i, char in enumerate(text):

            while node and char not in self.trie[node]:
                node = self.fail[node]

            node = self.trie[node].get(char, 0)

            for pat_idx in self.output[node]:
                pat = patterns[pat_idx]
                result.append((i - len(pat) + 1, pat))

        return result


# Example
patterns = ["he", "she", "his", "hers"]
text = "ahishers"

ac = AhoCorasick()

for i, p in enumerate(patterns):
    ac.add_word(p, i)

ac.build()

print(ac.search(text, patterns))