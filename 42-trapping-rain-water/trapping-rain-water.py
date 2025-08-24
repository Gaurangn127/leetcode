class Solution:
    def trap(self, height: List[int]) -> int:
        #using 2 pointers
        #the water stored AT a particular index, depends on:
        # the height of that column
        # the minimum b/w max height to the left and max height to the right
        # we move the pointer that is at the bottleneck (left pointer if at equal heights)
        # calucate the amount of water at that index, and add it to the volume

        l, r = 0, len(height) -1
        l_max, r_max = height[l], height[r]
        vol = 0

        while l < r:
            if l_max <= r_max :
                l += 1
                l_max = max(l_max, height[l])     #if height[i] > l_max, l_max = height[i], hence next line will give zero
                vol += l_max - height[l]         #if the height is greater than the height to its left till now, water at that index = 0
            else :
                r -= 1
                r_max = max(r_max, height[r])     #same logic as before
                vol += r_max - height[r]         #if the height is greater than any height to its right, there can be no water above the column
        
        return vol
