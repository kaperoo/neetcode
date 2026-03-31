class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        opt = []

        # for i in range(len(nums)):
        #     cumsum = 1
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         cumsum *= nums[j]
        #     opt.append(cumsum)
        cumsum = 1
        for n in nums:
            opt.append(cumsum)
            cumsum *= n

        cumsum = 1
        for i in range(len(nums)-1,-1,-1):
            opt[i] = opt[i]*cumsum
            cumsum *= nums[i]

        return opt