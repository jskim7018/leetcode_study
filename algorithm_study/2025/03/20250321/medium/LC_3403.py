class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        max_size = n - numFriends + 1

        curr_max = ""
        for i in range(n):
            if word[i:i+max_size] > curr_max:
                curr_max = word[i:i+max_size]
        return curr_max

