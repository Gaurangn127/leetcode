class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        vol = 0
        
        while l < r :
            curr = min( height[l], height[r] ) * ( r - l )
            
            if height[l] < height[r] :
                l += 1
            
            elif height[r] <= height[l] :
                r -= 1
            
            if curr > vol :
                vol = curr
        
        return vol