class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in s1:
            freq1[ord(c)-ord('a')] += 1

        start = 0
        end = start + len(s1) - 1

        for i in range(start, end+1):
            freq2[ord(s2[i])-ord('a')] += 1
        
        if freq1 == freq2:
                return True
        start += 1
        end += 1

        while end < len(s2):
            freq2[ord(s2[start-1])-ord('a')] -= 1
            freq2[ord(s2[end])-ord('a')] += 1

            if freq1 == freq2:
                return True
            end += 1
            start += 1

        return False