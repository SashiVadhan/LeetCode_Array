class Solution:
    def twoSum(self, nums: list, target: int):
        value_map = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in value_map:
                return [value_map[remaining], i]
            else:
                value_map[nums[i]] = i

# Explanation:
# Here they used a dictionary to store numbers and their indexes.
# "i" represents the index of the current number.
# "remaining" is the number needed to reach the target after subtracting target - nums[i].
# if "remaining" is already in the dictionary, we return both indexes. {key : value} -> key is in value postion.
# else we add the key value pair in the dictionary value_map[key] = index.             
#
# Time Complexity: O(n)
# Runtime: 0ms
# Memory: 20.6mb
