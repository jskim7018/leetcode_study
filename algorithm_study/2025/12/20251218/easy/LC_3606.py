from typing import List
import re


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str],
                        isActive: List[bool]) -> List[str]:
        n = len(code)

        valid_coupons = []
        valid_categories = {"electronics", "grocery", "pharmacy", "restaurant"}

        def is_code_valid(s: str) -> bool:
            return bool(re.fullmatch(r"[A-Za-z0-9_]+", s))

        for i in range(n):
            if is_code_valid(code[i]) and \
                    businessLine[i] in valid_categories and isActive[i]:
                valid_coupons.append((code[i], businessLine[i]))

        valid_coupons.sort(key=lambda x: (x[1], x[0]))

        return [coupon[0] for coupon in valid_coupons]
