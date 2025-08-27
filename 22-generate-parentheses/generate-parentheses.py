class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # we have n open parenthesis, and n closed parenthesis
        # (1) we can only open more if: no. of open parenthesis < n 
        # (2) we can only close if: no. of closing parenthesis < no. of open parenthesis
        # (3) we continue till: open count == close count == n

        stack = []
        res = []

        def backtrack(num_open, num_close) :
            if num_open < n :                           # (1)
                stack.append('(')
                backtrack(num_open + 1, num_close)
                stack.pop()
            
            if num_close < num_open :                   # (2)
                stack.append(')')
                backtrack(num_open, num_close + 1)
                stack.pop()
            
            if num_open == num_close == n :             # (3)
                res.append("".join(stack))
                return 
            
        backtrack(0, 0)
        return res