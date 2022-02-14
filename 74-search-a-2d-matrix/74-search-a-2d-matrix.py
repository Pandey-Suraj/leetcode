class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0 , len(matrix) - 1
        while (l<=r):
            mid = (l+r)//2
            
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                l = mid 
            elif matrix[mid][-1] > target:
                r = mid 
            if (l + r) // 2 in [0, mid, len(matrix) - 1]:
                break
                
            
        if target in matrix[l] or target in matrix[r]:
            return True 
        else:
            return False
            
        