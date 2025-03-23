class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bin_st = set()

        if k > len(s):
            return False

        binary = 0
        mask = 2**k-1
        for i in range(k):
            binary = binary << 1
            binary |= s[i] == '1'

        bin_st.add(binary)
        print(mask)
        for i in range(k, len(s)):
            binary = binary << 1
            binary |= s[i] == '1'
            binary &= mask
            bin_st.add(binary)
        if len(bin_st) == 2**k:
            return True
        else:
            return False
