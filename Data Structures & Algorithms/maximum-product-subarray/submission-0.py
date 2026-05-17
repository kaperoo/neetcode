class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [[0]*l for _ in range(l)]

        maximum = float('-inf')
        for x in range(l):
            for y in range(x,l):
                if x==y:
                    dp[x][y] = nums[x]
                else:
                    dp[x][y] = dp[x][y-1] * nums[y]

                maximum = max(maximum, dp[x][y])

        return maximum