class Solution:
    # TODO: recursive 한 방법도 가능. 나중에 해보기.
    def findKthBit(self, n: int, k: int) -> str:
        l = 1
        r = 1

        i = 1
        while r < k:
            r = r * 2 + 1
            i += 1

        curr = 1
        while l <= r:
            mid = (l+r)//2
            if mid == k:
                if l == r:
                    curr = (curr + 1) % 2
                return str(curr)
            elif mid < k:
                l = mid + 1
                curr = 0
            else:
                r = mid - 1
                curr = 1

        return ''