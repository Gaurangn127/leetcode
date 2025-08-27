class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0 :
            return False
        
        primes = [2, 3, 5]

        for p in primes :
            while n % p == 0 :
                n //= p
        
        return n == 1