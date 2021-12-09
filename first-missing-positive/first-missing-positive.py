class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted([num for num in nums if num > 0])
        if len(nums) == 0 or nums[0] != 1:
            return 1
        for i in range(len(nums) - 1):
            diff =  nums[i + 1] - nums[i]
            if diff > 1:
                return nums[i] + 1
        return nums[len(nums) - 1] + 1

        