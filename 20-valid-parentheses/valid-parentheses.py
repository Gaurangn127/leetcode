class Solution:
    def isValid(self, s: str) -> bool:
        # using data structure: stack 
        stack = []

        if len(s)%2 == 1 : return False
        elif s[0] in ')}]': return False

        for i in range(len(s)) :
            if s[i] in '({[':
                stack.append(s[i])

            # stack can be empty, in which case stack[-1] gives an index error
            # which is why we first check if stack as opening bracket

            elif (s[i] == ')') and ('(' in stack):
                if stack[-1] == '(':
                    stack.pop()
            
            elif (s[i] == '}') and ('{' in stack):
                if stack[-1] == '{':
                    stack.pop()

            elif (s[i] == ']') and ('[' in stack):
                if stack[-1] == '[':
                    stack.pop()
            
            else :
                return False
        
        if stack != []:
            return False

        return True
