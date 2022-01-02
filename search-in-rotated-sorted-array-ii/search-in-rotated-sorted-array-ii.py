class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()
            
        n = len(nums)
        l, r = 0 , len(nums) - 1
        while(l<=r):
            mid = (l+r)//2
            
            if nums[mid] == target:
                return True 
            if mid+1<= n-1  and nums[mid +1] == target:
                return True 
            if mid-1 >= 0 and nums[mid - 1 ] == target:
                return True 
            if nums[l] <= nums[mid]:
                if nums[l] <= target and nums[mid] >= target:
                    r = mid-1 
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1 
                    
                else:
                    r = mid - 1
            
        return False
            
        