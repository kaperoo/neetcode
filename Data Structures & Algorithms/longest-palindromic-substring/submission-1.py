class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        l = 0
        r = len(s)

        while l < r:
            for i in range(0,len(s)-r+1):
                if self.isPalindrome(s[l+i:l+r+i]):
                    return s[l+i:l+r+i]         

            r -= 1

    def isPalindrome(self,word):
        i = 0
        j = len(word)-1
        print(word)
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
    
        return True

