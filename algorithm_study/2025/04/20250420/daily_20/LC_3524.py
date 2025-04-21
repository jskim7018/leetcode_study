from typing import List

def find_x_values(nums: List[int], k: int) -> List[int]:
    # dp_prev[r] = number of subarrays ending at the previous index whose product % k == r
    dp_prev = [0] * k
    # result[x] = total number of subarrays (over all end positions) with product % k == x
    result = [0] * k

    for num in nums:
        v = num % k
        dp_curr = [0] * k

        # 1) Extend all subarrays ending at the previous index by multiplying v
        for r in range(k):
            cnt = dp_prev[r]
            if cnt:
                dp_curr[(r * v) % k] += cnt

        # 2) Add the single-element subarray [num] itself
        dp_curr[v] += 1

        # 3) Accumulate into the global result
        for x in range(k):
            result[x] += dp_curr[x]

        # 4) Shift for next iteration
        dp_prev = dp_curr

    return result

# Example usage:
if __name__ == "__main__":
    print(find_x_values([1,2,3,4,5], 3))       # [9, 2, 4]
    print(find_x_values([1,2,4,8,16,32], 4))   # [18, 1, 2, 0]
    print(find_x_values([1,1,2,1,1], 2))       # [9, 6]
