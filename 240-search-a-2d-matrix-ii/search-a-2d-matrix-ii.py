class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) 
        n = len(matrix[0])
        i, j = 0, n - 1         #using the top-right approach to find the desired element

        while i < m and j >= 0 :
            if target > matrix[i][j] :
                i += 1
            elif target < matrix[i][j] :
                j -= 1
            else :
                return True
        
        return False
