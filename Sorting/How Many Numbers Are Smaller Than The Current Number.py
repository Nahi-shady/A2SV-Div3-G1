class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        val = []
        for i in nums:
            sum = [k for k in nums if k < i]
            val.append(len(sum))
        return val