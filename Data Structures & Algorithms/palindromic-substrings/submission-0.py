class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        l=0
        r=len(s)
        count = 0
        while l<r:
            for i in range(0,len(s)-r+1):
                if self.isPalindrome(s[l+i:l+i+r]):
                    count += 1
            r-=1
        return count
        
        # dp = [[False]*len(s) for _ in range(len(s))]

    def isPalindrome(self, word):
        i=0
        j=len(word)-1
        while i<j:
            if word[i] != word[j]:
                return False
            i+=1
            j-=1
        return True
