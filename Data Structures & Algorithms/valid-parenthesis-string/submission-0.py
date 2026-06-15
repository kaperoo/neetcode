from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        joker = deque([])

        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) > 0:
                    stack.pop()
                elif len(joker) > 0:
                    joker.popleft()
                else:
                    return False
            else:
                joker.append(i)

        for s in stack[::-1]:
            if len(joker) > 0:
                if joker[-1] > s:
                    joker.pop()
                    stack.pop()
                else:
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        return False