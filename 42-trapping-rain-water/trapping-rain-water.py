class Solution:
    def trap(self, height: List[int]) -> int:
        #using 2 pointers
        #the water stored AT a particular index, depends on:
        # the height of that column
        # the minimum b/w max height to the left and max height to the right

        l, r = 0, len(height) -1
        l_max, r_max = height[l], height[r]
        vol = 0

        while l < r:
            if l_max <= r_max :
                l += 1
                l_max = max(l_max, height[l])
                vol += l_max - height[l]
            else :
                r -= 1
                r_max = max(r_max, height[r])
                vol += r_max - height[r]
        
        return vol