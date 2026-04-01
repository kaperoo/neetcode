class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        nums = []
        operations = set(["-", "+", "/", "*"])
        for i in range(len(tokens)):
            if tokens[i] not in operations:
                nums.append(int(tokens[i]))
            else:
                num2 = nums.pop()
                num1 = nums.pop()
                if tokens[i] == "+":
                    nums.append(num1+num2)
                elif tokens[i] == "-":
                    nums.append(num1-num2)
                elif tokens[i] == "/":
                    nums.append(int(num1/num2))
                else:
                    nums.append(num1*num2)
        return nums[-1]