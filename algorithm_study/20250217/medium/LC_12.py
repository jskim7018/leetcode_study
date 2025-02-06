class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_mp = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        ans = ""
        for k,v in symbol_mp.items():
            if num // k > 0:
                ans += v * (num // k)
                num -= num//k * k
        return ans
