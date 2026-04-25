class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.res = []
        self.recurse([],0)
        return self.res

    def recurse(self, pals, length):
        if length == len(self.s):
            self.res.append(pals)

        for i in range(length+1,len(self.s)+1):
            # print(self.s[length:i])
            if self.isPalindrome(self.s[length:i]):
                self.recurse(pals + [self.s[length:i]], i)
        

    def isPalindrome(self, word):
        i,j = 0, len(word)-1

        while i<j:
            if word[i] != word[j]:
                return False
            i+=1
            j-=1
        
        return True