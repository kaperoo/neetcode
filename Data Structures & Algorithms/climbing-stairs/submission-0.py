class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n

        for i in range(n):
            if i == 0:
                dp[0] = 1
                continue
            if i == 1:
                dp[1] = 2
                continue
            
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]