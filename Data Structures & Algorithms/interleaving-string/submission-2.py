class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]

        if len(s3) != len(s1) + len(s2):
            return False

        flag = False
        for i in range(len(s2)+1):
            for j in range(len(s1)+1):

                if i == j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    if s3.startswith(s1[:j]):
                        dp[i][j] = 1
                elif j == 0:
                    if s3.startswith(s2[:i]):
                        dp[i][j] = 1
                else:
                    if dp[i-1][j] == 1 and s2[i-1] == s3[i+j-1]:
                        dp[i][j] = 1
                    if dp[i][j-1] == 1 and s1[j-1] == s3[i+j-1]:
                        dp[i][j] = 1

        # print(dp)
        return bool(dp[i][j])


