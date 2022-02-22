class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums= sorted(nums)
        res, val = 0, 0 
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1] : 
                res +=1 
            val += res 
            # print(res,val)
        return val
        