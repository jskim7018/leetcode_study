class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        unionFind = MyUnionFind()

        for a,b in zip(s1, s2):
            unionFind.union(ord(a)-ord('a'), ord(b)-ord('a'))

        ans = []
        for ch in baseStr:
            ans.append(chr(unionFind.find(ord(ch)-ord('a')) + ord('a')))

        return ''.join(ans)


class MyUnionFind:

    def __init__(self):
        self.arr = list(range(26))

    def find(self, a: int) -> int:
        _next = a
        while self.arr[_next] < _next:
            _next = self.arr[_next]
        return _next

    def union(self, a: int, b: int):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root < b_root:
            self.arr[a_root] = a_root
            self.arr[b_root] = a_root
            self.arr[a] = a_root
            self.arr[b] = a_root
        else:
            self.arr[a_root] = b_root
            self.arr[b_root] = b_root
            self.arr[a] = b_root
            self.arr[b] = b_root
