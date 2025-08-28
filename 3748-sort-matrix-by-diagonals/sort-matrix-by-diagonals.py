class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)

        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])

        for key in diagonals :
            if key < 0 :
                diagonals[key].sort()
            else :
                diagonals[key].sort(reverse = True)

        for i in range(n) :
            for j in range(n) :
                grid[i][j] = diagonals[i-j].pop(0)
        
        return grid