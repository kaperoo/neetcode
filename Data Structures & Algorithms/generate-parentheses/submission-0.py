class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.recurse(n,'',0,0)
        return self.res
        
    def recurse(self, n, s, d, b):
        if d == b == n:
            self.res.append(s)
            return

        if d < n:
            self.recurse(n,s+'(',d+1,b)
        if b < d:
            self.recurse(n,s+')',d,b+1)
        
        return
