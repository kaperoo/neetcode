class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.recurse(nums, target)            

    def recurse(self, nums, target):
        opts = []
        for e,i in enumerate(nums):
            if i == target:
                opts.append([i])
            elif i < target:
                res = self.recurse(nums[e:],target-i)
                for o in res:
                    opts.append(o+[i])
            
        return opts