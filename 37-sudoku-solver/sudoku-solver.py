class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        # previously i was checking validity or a number using for loops, 
        # to optimize, i use sets

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        empty = []


        for i in range(9) :
            for j in range(9) :
                if board[i][j] == "." :
                    empty.append((i, j))

                else :
                    ch = board[i][j]
                    rows[i].add(ch)
                    cols[j].add(ch)
                    squares[(i // 3) * 3 + (j // 3)].add(ch)
        

        def isValid(r, c, ch):
            sq = (r // 3) * 3 + (c // 3)
            return ch not in rows[r] and ch not in cols[c] and ch not in squares[sq]
        

        def backtrack(index = 0):
            if index == len(empty) :
                return True

            r, c = empty[index]
            sq = (r // 3) * 3 + (c // 3)

            for ch in "123456789" :
                if isValid(r, c, ch) :
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch) 
                    squares[sq].add(ch)

                    if backtrack(index + 1) :
                        return True
                    
                    board[r][c] == "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    squares[sq].remove(ch)

            return False
        
        backtrack()