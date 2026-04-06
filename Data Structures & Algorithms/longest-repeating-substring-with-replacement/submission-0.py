class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        count = {}
        max_w = k + 1

        i = 0
        win = 0
        while i+win != len(s):
            if i == 0 and win ==0:
                m_freq = s[0]
                count[s[0]] = 1
                win += 1
                continue
            
            count[s[i+win]] = count.get(s[i+win], 0) + 1
            if count[s[i+win]] > count[m_freq]:
                m_freq = s[i+win]
            
            if count[m_freq] + k < win+1:
                count[s[i]] -= 1
                i+=1
            else:
                max_w = win+1
                win += 1

        return max_w