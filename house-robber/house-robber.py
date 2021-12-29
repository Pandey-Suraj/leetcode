class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        dp = [0]* length
        dp[0],dp[1] = nums[0],max(nums[0],nums[1])
        for i in range(2,length):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
            
        return dp[-1]
        