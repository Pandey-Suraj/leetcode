class Solution:
    def findMin(self, nums: List[int]) -> int:
        # minimum = nums[0]
        # l,r = 0 , len(nums)-1                
        # while (l<=r):
        #     mid = l + (r-l)//2
        #     if nums[mid] > nums[r]:
        #         l = mid+1
        #     else:
        #         r = mid-1
        #     minimin = min(minimum, nums[mid])
        # return minimum
    
        minimum = nums[0] # initialize with first value
        lo = 0
        hi = len(nums)-1
        
        while lo <= hi:
            mid = lo + (hi-lo)//2
            print(mid,nums[mid])
            if nums[mid] > nums[hi]: # mid is taller than hi value
                lo = mid+1 # search right
            else: # mid is smaller than hi value
                hi = mid-1 # search left
            minimum = min(minimum, nums[mid])  
        return minimum