class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prev = None
        current = nums[0]
        nums[0] *= -1

        while True:
            if current <0:
                return prev
            prev = current
            current = nums[current]
            nums[prev] *= -1
