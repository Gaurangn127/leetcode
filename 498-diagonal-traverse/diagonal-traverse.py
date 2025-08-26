class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        i, j = 0, 0
        going_up = True 
        
        res = []

        while len(res) < (m * n) :
            if going_up :
                while i >= 0 and j < n :
                    res.append(mat[i][j])
                    i -= 1
                    j += 1
                
                if j < n :
                    i += 1
                else :
                    j -= 1
                    i += 2
                
                going_up = False
            
            else :
                while j >= 0 and i < m :
                    res.append(mat[i][j])
                    i += 1
                    j -= 1
                
                if i < m :
                    j += 1
                else :
                    j += 2
                    i -= 1
                
                going_up = True
        
        return res