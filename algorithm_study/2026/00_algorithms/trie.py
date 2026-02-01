class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children = {} # next가 아니라 children으로 이름 지으면 좋을듯.
        self.is_end = False

# TrieNode를 기반으로 Trie 자료구조를 만들면 됨.
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
