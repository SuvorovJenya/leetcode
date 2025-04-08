class Solution:
    def twoSum(self, nums, target):
        dict_nums = {}

        for i in nums:
            dict_nums[i] = nums.index(i)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and dict_nums[diff] != i:
                return [i, dict_nums[diff]]
        return []