class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        m = self.stack[0]
        for i in range(1, len(self.stack)):
            if self.stack[i] < m:
                m = self.stack[i]
        return m

        
