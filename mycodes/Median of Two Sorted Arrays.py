class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        print(length)
        if length%2 != 0:
            return nums1[(length-1)//2]
        else:
            return (nums1[ (length//2) - 1 ] + nums1[ length//2 ] )/2

# Time Complexity: O((m+n) log(m+n))
# 3ms
# 19.5mb
