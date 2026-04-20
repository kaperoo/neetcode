class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.recurse(candidates,target)


    def recurse(self, nums, target):
        prev = None
        opts = []
        for i,n in enumerate(nums):
            
            if len(nums) == 0:
                return []

            if prev == n:
                continue
            prev = n

            if target-n == 0:
                opts.append([n])
                break
            elif target-n<0:
                break
            else:
                os = self.recurse(nums[i+1:],target-n)
                for o in os:
                    opts.append(o+[n])
            
        return opts
