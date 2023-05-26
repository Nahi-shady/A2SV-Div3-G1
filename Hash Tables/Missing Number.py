class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        y = sum(range(0,len(nums)))
        x = sum(nums)

        return y - x