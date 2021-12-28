class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def addRange(i,j):
            while i>=0 and nums[i]==target:
                i-=1
            while j<len(nums) and nums[j]==target:
                j+=1

            return [i+1,j-1]
        
        lo,hi = 0,len(nums)-1
        while(lo<=hi):
            mid = (lo+hi)//2
            if nums[mid] == target:
                return addRange(mid,mid)
            elif nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1 
            
        return (-1,-1)
        
