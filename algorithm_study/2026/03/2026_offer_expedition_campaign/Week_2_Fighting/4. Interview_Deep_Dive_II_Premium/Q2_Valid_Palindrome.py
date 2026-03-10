class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TODO: filter가 아니라 two-pointer로 대상이 아니면 넘어가는 방식도 가능.
        # two-pointer로 하면 메모리 절약 가능
        s_filtered = []
        for ch in s:
            if ch.isalnum():
                s_filtered.append(ch.lower())

        n = len(s_filtered)

        for i in range(n//2):
            if s_filtered[i] != s_filtered[n-i-1]:
                return False

        return True
