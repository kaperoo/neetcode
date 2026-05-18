class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.words = wordDict
        self.idxs = {}

        return self.recurse(0)

    def recurse(self,idx):
        if idx == len(self.s):
            return True

        for w in self.words:
            l = len(w)
            if self.s[idx:idx+l] == w and self.idxs.get(idx+l,True):
                if self.recurse(idx+l):
                    return True
        
        self.idxs[idx] = False
        return False