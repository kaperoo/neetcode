class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        opts = set()

        nums.sort()

        prev_l = None
        for l in range(len(nums)-2):
            if nums[l] == prev_l:
                continue
            
            m = l+1
            r = len(nums)-1

            while m < r:
                if nums[m] + nums[r] + nums[l] == 0:
                    opts.add((nums[l],nums[m],nums[r]))
                    r -= 1
                    m += 1
                elif nums[m] + nums[r] + nums[l] > 0:
                    r -= 1
                elif nums[m] + nums[r] + nums[l] < 0:
                    m += 1
            prev_l = nums[l]

        fin = list(map(lambda x: list(x), list(opts)))
        return fin