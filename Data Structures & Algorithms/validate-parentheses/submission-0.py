class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in [')',']','}']:
                if len(stack) != 0:
                    p = stack.pop()
                    if (p == "(" and b == ")") or (p == "[" and b == "]") or (p == "{" and b == "}"):
                        continue
                return False
            else:
                stack.append(b)

        if len(stack) == 0:
            return True
        else:
            return False