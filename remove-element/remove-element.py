class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # base cases
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                if nums[0] == val:
                    return 0
                return 1

            # for lists having more than one element
            i = 0
            while i < len(nums):
                if nums[i] == val:
                    nums.pop(i)
                    continue
                i += 1
            return len(nums) 