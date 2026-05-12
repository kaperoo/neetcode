class Solution:

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        nums2 = nums.copy()
        nums2.pop()
        for i in range(3,len(nums)):
            if i == 3:
                nums[i] += nums[i-2]
                continue 
            nums[i] += max(nums[i-2],nums[i-3])

        for i in range(2,len(nums2)):
            if i == 2:
                nums2[i] += nums2[i-2]
                continue 
            nums2[i] += max(nums2[i-2],nums2[i-3])

        return max(max(nums[-1],nums[-2]),max(nums2[-2],nums2[-1]))
