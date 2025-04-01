class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)

        def isPalindrome(s: str) -> bool:
            n = len(s)
            for i in range(n//2):
                if s[i] != s[n-i-1]:
                    return False

            return True

        if isPalindrome(a) or isPalindrome(b):
            return True

        l = 0
        r = n-1
        while l < n and r >= 0 and a[l] == b[r]:
            l+=1
            r-=1
        if isPalindrome(a[l:r+1]) or isPalindrome(b[l:r+1]):
            return True
        l = 0
        r = n - 1
        while b[l] == a[r]:
            l += 1
            r -= 1
        if isPalindrome(a[l:r+1]) or isPalindrome(b[l:r+1]):
            return True

        return False