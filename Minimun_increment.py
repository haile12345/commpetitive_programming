class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        low = -math.inf
        for x in nums:
            low = max(low+1, x)
            res += low - x
        return res
