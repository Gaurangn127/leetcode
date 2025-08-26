class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxArea, maxDiag = 0, 0

        for a,b in dimensions:
            d = a**2 + b**2
            maxDiag, maxArea = max((maxDiag, maxArea), (d, a*b))

        return maxArea