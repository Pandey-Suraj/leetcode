class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         orignal = []
#         output = False
#         i = 0
#         while i < len(nums):
#             if nums[i] in orignal:
#                 output = True
#             orignal.append(nums[i])
        
#             i += 1
        
        
#         return output
          return not len(nums) == len(set(nums))