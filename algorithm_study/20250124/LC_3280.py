class Solution:
    def convertDateToBinary(self, date: str) -> str:
        split_date = date.split('-')

        list = []
        for d in split_date:
           list.append(bin(int(d))[2:])

        return '-'.join(list)