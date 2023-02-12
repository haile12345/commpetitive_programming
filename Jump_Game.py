class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        D = [-float('inf')] * (n)
        
		# set initial value
        D[0] = nums[0]
        
        for i in range(1, n):
            maxValue = -float('inf')
            
			# get max score from D[i-1], D[i-2], .., D[i-k]
            for j in range(1, k+1):
                if i-j < 0: continue
                maxValue = max(maxValue, D[i-j])
            
			# add score of current index to maximum score we've got
            D[i] = maxValue + nums[i]
        
        return D[n-1]
