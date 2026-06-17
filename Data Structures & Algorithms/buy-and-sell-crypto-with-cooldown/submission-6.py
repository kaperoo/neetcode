class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [[0]*l for _ in range(l)]

        max_profit = 0
        for i in range(l):
            for j in range(i+1,l):
                local_diff = prices[j] - prices[i]
                # local_diff = max(prices[j] - prices[i], dp[i][j-1])
                run = dp[i][j-1]

                if i >= 3:
                    prev_diff = dp[i-3][i-2]
                    dp[i][j] = max(local_diff+prev_diff,max(run,local_diff))
                else:
                    dp[i][j] = max(local_diff,run)
                
                if i >= 1:
                    dp[i][j] = max(dp[i-1][j], dp[i][j])
                max_profit = max(max_profit,dp[i][j])

        # print(dp)
        return max_profit

#      1  1000     1 1000     1 1000     1 1000
# 1   [0,  999,    0, 999,    0, 999,    0, 999], 
# 1000[0,    0, -999,   0, -999,   0, -999,   0], 
# 1   [0,    0,    0, 999,    0, 999,    0, 999], 
# 1000[0,    0,    0,   0,    0, 999,    0, 999], 
# 1   [0,    0,    0,   0,    0, 999,    0, 999], 
# 1000[0,    0,    0,   0,    0,   0,    0, 999], 
# 1   [0,    0,    0,   0,    0,   0,    0, 999], 
# 1000[0,    0,    0,   0,    0,   0,    0,   0]

[0, 999, 999, 999, 999, 999, 999, 999], 
[0,   0,   0,   0,   0,   0,   0,   0], 
[0,   0,   0, 999, 999, 999, 999, 999], 
[0,   0,   0,   0,   0, 999, 999, 999], 
[0,   0,   0,   0,   0, 999, 999, 999], 
[0,   0,   0,   0,   0,   0,   0, 999], 
[0,   0,   0,   0,   0,   0,   0, 999], 