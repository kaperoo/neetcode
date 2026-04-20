class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def recurse(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            opt = []
            for i,n in enumerate(nums):
                os = recurse(nums[:i] + nums[i+1:])
                for o in os:
                    opt.append(o+[n])

            return opt

        return recurse(nums)

                