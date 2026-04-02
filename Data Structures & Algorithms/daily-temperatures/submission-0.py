class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures

        l = len(temperatures)
        opts = [0]*l
        stack = []

        for i in range(l):
            while stack and temp[i] > stack[-1][0]:
                t = stack.pop()
                opts[t[1]] = i-t[1]

            stack.append((temp[i],i))

        return opts

        
