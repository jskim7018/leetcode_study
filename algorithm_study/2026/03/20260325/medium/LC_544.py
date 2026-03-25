class Solution:
    def findContestMatch(self, n: int) -> str:

        curr_rank = [(str(i)) for i in range(1,n+1)]

        while len(curr_rank) > 1:
            new_rank = []

            cr_n = len(curr_rank)
            for i in range(cr_n//2):
                match1 = curr_rank[i]
                match2 = curr_rank[cr_n-i-1]

                new_rank.append("(" + match1 + "," + match2 + ")")
            curr_rank = new_rank

        return curr_rank[0]
