from math import *
class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2 == 1:
            n = (len(nums3) // 2) 
            return nums3[n]

        else:
             n = (len(nums3) // 2) - 1
             return float(nums3[n] + nums3[n + 1])/2

#         nums3 = set(nums3)
#         print(nums3)
#         if len(nums3) == 2:
#             return (nums3[0] + nums3[1])/2
        
#         if len(nums3)//2 == 0:
#             n = len(nums3)//2
#             if nums3[0] == nums3[n-1]:
#                 median = nums3[n]
#             else:
#                 meidan = (nums3[n] + nums3[n-1])/2
            
#         else:
#             n = floor(len(nums3)//2)
#             if nums3[0] == nums3[n-1]:
#                 median = nums3[n]
#             else:
#                 median = (nums3[n] + nums3[n-1])/2
        
       
#         return(median)
