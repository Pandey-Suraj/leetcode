class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        l,r = 0,n
        
        while(l<=r):
            
            total = (l+r)//2
            
            if nums[total] == target:
                return total 
            
            elif target > nums[total]:
                l = total + 1
            
            elif target < nums[total]:
                r = total - 1
        else:
            return -1
                
                
        