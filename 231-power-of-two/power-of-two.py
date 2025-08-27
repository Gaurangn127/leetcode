class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
                
        for i in range(31) :
            power = 2 ** i
            if n == power :
                return True
        
        return False
