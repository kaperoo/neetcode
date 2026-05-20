class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        self.nums = nums
        if s%2 == 1:
            return False

        return self.recurse(s/2,0)

    def recurse(self, total, idx):
        if total == 0:
            return True

        for i in range(idx,len(self.nums)):
            if self.nums[i] <= total:
                if self.recurse(total-self.nums[i],i+1):
                    return True
        
        return False
        