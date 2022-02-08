class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums) - 1 
        l,r = 0 , n 
        
        while(l<=r):
            
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return l
           
                
        
        

        

                
            
        
        