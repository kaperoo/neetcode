class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s)-1,-1,-1):
            for j in range(len(s)-i):
                if len(set(s[j:j+i+1])) == i+1:
                    return i+1
        return 0
                