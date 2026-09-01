class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Explanation:
# Here I used 2 for loops.
# "i" represents the index of the first number.
# "j" starts from "i + 1", because we only need to check elements after i.
# If nums[i] + nums[j] equals target, we return their indices.
#
# Time Complexity: O(n²) 
# 1750ms
