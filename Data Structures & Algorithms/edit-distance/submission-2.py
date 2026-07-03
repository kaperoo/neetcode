class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf')]*len(word1) for _ in range(len(word2))]

        if not (word1 or word2):
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1) 

        for i in range(len(word2)):
            for j in range(len(word1)):
                if j == i == 0:
                    dp[i][j] = 0 if word1[j] == word2[i] else 1
                elif i == 0:
                    dp[i][j] = j if word1[j] == word2[i] else dp[i][j-1] + 1
                elif j == 0:
                    dp[i][j] = i if word1[j] == word2[i] else dp[i-1][j] + 1
                else:
                    dp[i][j] = dp[i-1][j-1] if word1[j] == word2[i] else min([dp[i-1][j-1],dp[i-1][j],dp[i][j-1]]) +1

        return dp[i][j]
                