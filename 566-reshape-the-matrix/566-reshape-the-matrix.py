class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        l = []
        output = []
        
        for i in mat:
            for j in i:
                l.append(j)
    
        if len(l) != r * c:
            return mat
        
        for i in range(0,len(l),c):
            output.append(l[i:i+c])
        return output
            
            
        