class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):  # can place?
                n -= 1
                if n == 0: return True
                flowerbed[i] = 1  # palce!
        return False
        
#         length = len(flowerbed) - 1
        
#         for i in range(length):
#             if i == 0:
#                 if flowerbed[i+1] == 0 and flowerbed[i] == 0:
#                     flowerbed[i] = 1
#                     n -= 1 
            
#             if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
#                 flowerbed[i] = 1
#                 n -= 1
            
#             if i == length:
#                 if flowerbed[length] == 0 and flowerbed[length+1] == 0:
#                     flowerbed[length+1] = 1
#                     n -= 1
                    
                
#         if n == 0 :
#             return True 
#         else:
#             return False
            
        