class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        # Merge sort counting.

        arr = [a - b for a, b in zip(nums1, nums2)]

        def merge_sort(l, r):
            if l >= r:
                return 0

            mid = (l + r) // 2
            count = merge_sort(l, mid) + merge_sort(mid + 1, r)

            # count valid pairs
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and arr[i] > arr[j] + diff:
                    j += 1
                count += (r - j + 1)

            # merge step
            temp = []
            i, j = l, mid + 1
            while i <= mid and j <= r:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= r:
                temp.append(arr[j])
                j += 1

            for i in range(len(temp)):
                arr[l + i] = temp[i]

            return count

        return merge_sort(0, len(arr) - 1)