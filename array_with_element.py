class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Algorithm: Time = O(n); Space = O(1); Algo Credits @bangoc
        # 1. We don't want any ascending or descending patterns among 
        #    3 consequtive elements, so we need to break them by swapping
        # 2. Get the 3 elements, (prev, cur, nxt)
        # 3. If these three are in ascending or descending order
        #    i,e. prev < cur < nxt or prev > cur > nxt
        #    then swap the cur and nxt elements
        # 4. Repeat this for entire array

        def swap(l, r):
            nums[l], nums[r] = nums[r], nums[l]
            
        n = len(nums)
        for i in range(1, n-1):
            prev, cur, nxt = nums[i-1], nums[i], nums[i+1]

            if prev < cur < nxt or prev > cur > nxt:
                swap(i+1, i)
                
        return nums
