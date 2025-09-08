class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res = n
        res -= 1

        while ('0' in str(res)) or ('0' in str(n - res)):
            res -= 1
        
        return [res, n - res]