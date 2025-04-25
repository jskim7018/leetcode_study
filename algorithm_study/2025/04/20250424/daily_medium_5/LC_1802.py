class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def get_rest(size, idx_num)->int:
            if size <= idx_num:
                ret = (((idx_num-size+1) + (idx_num))*size)//2
            else:
                ret = ((idx_num)*(idx_num+1))//2
                size -= idx_num
                ret += size
            return ret

        l = 1
        r = maxSum

        ans = 1
        while l <= r:
            mid = (l+r)//2
            if mid-1 <= 0:
                l = mid + 1
                continue
            curr = mid + get_rest(index,mid-1) + get_rest(n-index-1,mid-1)
            if curr < maxSum:
                ans = mid
                l = mid + 1
            elif curr > maxSum:
                r = mid - 1
            else:
                ans = mid
                break

        return ans
