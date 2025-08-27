class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9 :
            S = 0 

            while num > 0 :
                S += num % 10
                num = num // 10

            num = S 
        
        return num