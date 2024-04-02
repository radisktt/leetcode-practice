from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        queue = []
        for token in tokens:
            if token == '+':
                x = queue.pop();y = queue.pop()
                queue.append(x+y)
            elif token == '-':
                y = queue.pop();x = queue.pop()
                queue.append(x-y)
            elif token == '*':
                x = queue.pop();y = queue.pop()
                queue.append(x*y)
            elif token == '/':
                x = queue.pop();y = queue.pop()
                queue.append(int(y/x))
            else: queue.append(int(token))
        return queue.pop()