class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        L, R = 0, len(height) - 1
        tallest = max(height)
        while L < R:
            area = (R - L)*min(height[L], height[R])
            maxi = max(maxi,area)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
            if tallest * (R - L) <= maxi:
                break

        return maxi

# explanation:
"""
This code also runs without checking the tallest, i.e. without checking
the condition "tallest * (R - L) <= maxi".

But in that case, the time taken can be higher because we have to check
all the remaining possible positions even when we already know that
none of them can give a better answer.  ->  (53ms)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        L, R = 0, len(height) - 1
        while L < R:
            area = (R - L)*min(height[L], height[R])
            maxi = max(maxi,area)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return maxi

The "tallest * (R - L) <= maxi" condition helps us stop early when the
maximum possible area from the remaining width cannot exceed maxi.
"""
# Time Complexity: O(n)
# 3ms
# 29.4mb
