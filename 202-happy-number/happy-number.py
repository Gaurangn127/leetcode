class Solution:
    def isHappy(self, n: int) -> bool:

        found = set()

        while n not in found :
            found.add(n)

            S = 0
            while n > 0 :
                S += (n % 10) ** 2
                n = n // 10

            if S == 1 :
                return True
            
            n = S
        
        return False