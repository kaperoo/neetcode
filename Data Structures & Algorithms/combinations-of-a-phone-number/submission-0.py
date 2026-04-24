class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        self.alpha={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.result = ['']
        self.digits = digits


        self.recurse(0)

        return self.result

    def recurse(self,idx):
        if idx > len(self.digits) -1:
            return
        
        temp = []
        for c in self.alpha[self.digits[idx]]:
            for o in self.result:
                temp.append(o+c)

        self.result = temp
        self.recurse(idx+1)