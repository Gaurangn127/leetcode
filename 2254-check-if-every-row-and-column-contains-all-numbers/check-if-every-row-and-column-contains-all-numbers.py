class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        required = set(range(1, n + 1))

        for r in range(n) :
            if set(matrix[r]) != required :
                return False
        
        for c in range(n) :
            col = [matrix[r][c] for r in range(n)]
            if set(col) != required :
                return False
        
        return True
        