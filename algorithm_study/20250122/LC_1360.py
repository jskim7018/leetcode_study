from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Define the format of the string
        date_format = "%Y-%m-%d"

        date1 = datetime.strptime(date1, date_format).date()
        date2 = datetime.strptime(date2, date_format).date()

        return abs((date2 - date1).days)
