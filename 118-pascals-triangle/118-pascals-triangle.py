class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return output
        else:
            for i in range(1,numRows-1):
                # print(output[i])
                length = len(output[i]) -1
                # print(length)
                d = []
                d.append(1)
                for j in range(length):
                    total = output[i][j] + output[i][j+1]
                    d.append(total)
                    # print(total)
                d.append(1)
                output.append(d)
        return output
                    
                
                
                
                