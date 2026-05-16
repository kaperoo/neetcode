class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.ams = {}
        return self.dfs(amount)

    def dfs(self,a):
        if a == 0:
            return 0
        if a in self.ams:
            return self.ams[a]

        minimum = float('inf')
        for c in self.coins:
            if a-c<0:
                continue
            
            opt = self.dfs(a-c)
            if opt != -1:
                minimum = min(minimum, opt)

        if minimum == float('inf'):
            self.ams[a] = -1
            return -1
        else:
            self.ams[a] = minimum + 1
            return minimum + 1
