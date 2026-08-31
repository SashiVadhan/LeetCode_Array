class Solution:
    def twoSum(self, nums: list, target: int):
        value={}
        for i in range(len(nums)):
            remaining= target - nums[i]
            if remaining in value:
                return [value[remaining], i]
            else:
                value[nums[i]]=i