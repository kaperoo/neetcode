class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [[0]*len(coins) for _ in range(amount)]

        for i in range(amount):
            for j in range(len(coins)):
                cell_total = 0
                sub = i+1 - coins[j] 
                if sub >= 0:
                    if sub == 0:
                        cell_total += 1
                    # else:
                    #     cell_total += dp[sub-1][-1]
                    else:
                        cell_total += dp[i-coins[j]][j]

                
                if j>0:
                    cell_total += dp[i][j-1]

                dp[i][j] = cell_total

        # print(dp)
        return dp[-1][-1]



#   1  2  3
# 1 1  1  1 
# 2 1  2  2
# 3 1  2  3
# 4 1  3  4

