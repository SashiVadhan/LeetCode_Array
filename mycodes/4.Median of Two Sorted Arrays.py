class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1 + nums2)
        n = len(arr)
        if n % 2:
            return arr[n // 2]
        return (arr[n // 2 - 1] + arr[n // 2]) / 2

# Time Complexity: O((m+n) log(m+n))
# 0ms
# 19.4mb
