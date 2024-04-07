class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = [];check = []
        for i in range(len(s)):
           if s[i] == '*':
               check.append(i)
           elif s[i] == '(':
               stack.append(i)
           else:
               if stack:
                   stack.pop()
               elif check > 0:
                   check.pop()
               else:return False
        while stack and check:
            if stack.pop() > check.pop():
                return False
        return not stack