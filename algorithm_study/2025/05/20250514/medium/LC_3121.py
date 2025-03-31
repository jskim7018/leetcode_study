
# TODO: Study more concise answer
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        isLowerVisited = [False] * 26
        isUpperVisited = [False] * 26
        notSpecialLetterSet = set()
        all_lower_letters = set()
        for c in word:
            if c.lower() in notSpecialLetterSet:
                continue
            if ord('a') <= ord(c) <= ord('z'):
                all_lower_letters.add(c)
                if isUpperVisited[ord(c) - ord('a')]:
                    notSpecialLetterSet.add(c)
                elif not isLowerVisited[ord(c) - ord('a')]:
                    isLowerVisited[ord(c) - ord('a')] = True
            else:
                all_lower_letters.add(c.lower())
                if not isLowerVisited[ord(c) - ord('A')]:
                    notSpecialLetterSet.add(c.lower())
                elif not isUpperVisited[ord(c) - ord('A')]:
                    isUpperVisited[ord(c) - ord('A')] = True
        for letter in all_lower_letters:
            if not isUpperVisited[ord(letter) - ord('a')]:
                notSpecialLetterSet.add(letter)
        return len(all_lower_letters) - len(notSpecialLetterSet)
