class Solution(object):
    def targetIndices(self, nums, target):
        lowVals = 0; repOfTg = 0
        for val in nums:
            if val < target:
                lowVals += 1
            elif val == target:
                repOfTg += 1
        ans = []
        for _ in range(repOfTg):
            ans.append(lowVals)
            lowVals += 1
        return ans
