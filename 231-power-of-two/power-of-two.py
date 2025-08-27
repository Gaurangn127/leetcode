class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
                
        if n == 1 :
            return True

        if n % 2 == 1 or n <= 0 :
            return False
        
        while n > 1 :
            if n % 2 == 1 :
                return False
            n = n / 2
        
        return True