import typing as List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            stack.append(x)# stack[n-2] < 0 -> bo qua
            while len(stack)>1 and stack[len(stack)-1]*stack[len(stack)-2]< 0 and stack[len(stack)-2] >0:
                x= stack.pop()
                y = stack.pop()
                if abs(x)!=abs(y): stack.append(x if abs(x)>abs(y) else y)
        return list(stack)