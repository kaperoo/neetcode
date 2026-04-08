class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        minimum = nums[mid]


        while left < right:
            if nums[mid] <= nums[-1]:
                right = mid -1
            elif nums[mid] > nums[-1]:
                left = mid + 1

            mid = (left+right)//2
            if nums[mid]<minimum:
                minimum = nums[mid]

        return minimum