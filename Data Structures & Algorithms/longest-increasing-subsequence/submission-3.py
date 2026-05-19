class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.seen = {}
        return self.recurse(float('-inf'),0) -1

    def recurse(self,prev,idx):
        if idx == len(self.nums):
            return 1
        elif idx in self.seen:
            return self.seen[idx]

        length = 0
        for i,n in enumerate(self.nums[idx:]):
            if n > prev:
                length = max(length, self.recurse(n,idx+i+1))

        self.seen[idx] = length + 1
        return length + 1