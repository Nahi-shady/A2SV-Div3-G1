class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {}
        for x, y in reversed(operations): mp[x] = mp.get(y, y)
        return [mp.get(x, x) for x in nums]