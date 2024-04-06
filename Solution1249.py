class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = 0; remove = set()
        for i in range(len(s)):
            if s[i] == ')':
                if not stack:
                    remove.add(i)
                else: stack.pop()
            elif s[i] =='(':
                stack.append(i)
        remove.update(stack)
        return "".join(s[i] for i in range(len(s)) if i not in remove)