class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1 or n == 7 : 
            return True
        
        elif n < 10 : 
            return False

        else :
            S = 0
            while n > 0 :
                S += (n % 10) ** 2
                n = n // 10
            
            return self.isHappy(S)
                