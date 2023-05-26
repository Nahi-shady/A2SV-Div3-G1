class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            expected = target - nums[i]
            if expected in nums and i != nums.index(expected):
                return [i, nums.index(expected)]