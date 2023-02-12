class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height)-1 # start at ends of array
        
        max_vol = 0 # max vol is 0 to start
        
        while left < right:
            lh, rh = height[left], height[right] # store heights
            
            vol = min(lh, rh) * (right - left) # calculate current volume
            
            if vol > max_vol: # set max vol if current vol > max vol
                max_vol = vol
                
            if lh >= rh: # left side is taller
                while left < right and height[right] <= rh: # volume only potentially gets bigger if we find a taller right side, move over until taller
                    right -= 1
            else:
                while left < right and height[left] <= lh: # same for left, need to find a taller left if we want to increase volume
                    left += 1
                
        return max_vol
