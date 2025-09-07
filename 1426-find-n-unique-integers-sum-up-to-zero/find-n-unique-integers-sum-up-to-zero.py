class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1,n):
            res.append(i)
        
        res.append(n * (1 - n)//2)

        return res
