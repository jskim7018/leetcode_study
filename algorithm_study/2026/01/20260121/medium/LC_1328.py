class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        n = len(palindrome)

        ans = list(palindrome)
        is_replaced = False
        for i in range(n//2):
            if palindrome[i] != 'a':
                ans[i] = 'a'
                is_replaced = True
                break

        if not is_replaced:
            ans[-1] = 'b'

        return ''.join(ans)
