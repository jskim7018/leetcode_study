class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_dict = dict()

        for a, b in zip(s, t):
            if a in iso_dict.keys():
                if b != iso_dict[a]:
                    return False
            elif b in iso_dict.values():
                return False
            else:
                iso_dict[a] = b

        return True
